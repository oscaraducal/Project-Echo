# Event Flow

Status: Active  
Version: 1.0  
Mission: PE-014  

---

# Purpose

Documented runtime event chains for core systems, matching MCP graph inspection (PE-014).

---

# Movement

```text
Hardware key/axis
  → Enhanced Input Local Player Subsystem (IMC_Player active)
  → IA_Move Triggered
  → BP_PlayerCharacter Enhanced Input event
  → HandleMoveInput(ActionValue)
  → AddMovementInput (camera-relative when ControlRotation path is correct)

IA_Look Triggered
  → HandleLookInput
  → Controller yaw / pitch

IA_Jump Started / Completed
  → Jump / StopJumping

IA_Sprint Started / Completed
  → StartSprint / StopSprint
  → CanStartSprint? → ApplySprintSpeed / ApplyWalkSpeed
```

**Registration chain**

```text
BP_PlayerController OnPossess
  → LocalPlayer GetEnhancedInputLocalPlayerSubsystem
  → AddMappingContext(IMC_Player)

BP_PlayerController BeginPlay
  → DelayUntilNextFrame
  → IsLocalPlayerController?
  → same AddMappingContext path (redundancy; PE-013C / BUG-008)
```

---

# Interaction

```text
IA_Interact Started
  → BPC_Interaction.TryInteract
  → GetOwner → GetActorEyesViewPoint
  → SphereTraceByChannel (radius TraceRadius, dist TraceDistance, Visibility)
  → BreakHitResult → HitActor
  → Set CurrentTarget
  → DoesObjectImplementInterface(BPI_Interactable)?
  → [optional] CanInteract(Owner)
  → Interact(Owner)
  → Target EventInteract / override logic
```

**Examples after Interact**

| Target | Chain |
|--------|-------|
| `BP_Door` | Toggle `IsOpen` / door motion |
| `BP_LockedDoor` | Inventory `HasItem(RequiredItemID)` → unlock/open |
| `BP_FuelCan` | `BPC_Inventory.AddItem(ItemData)` → Destroy |
| `BP_KeyItemPickup` | AddItem → `SetObjective("Unlock the secured door")` → Destroy |
| `BP_FlashlightPickup` | `GiveFlashlight` → `SetObjective("Read the maintenance log")` → Destroy |
| `BP_NotePickup` | See Notes chain |
| `BP_Generator` | See Generator chain |

---

# Generator

```text
EventInteract(Interactor)
  → GetComponentByClass BPC_Inventory + BPC_Objective
  → switch GeneratorState
      case Running (2):
        Print "Generator already running."
      case Off (0):
        HasItem("FuelCan")?
          Yes: RemoveItem("FuelCan") → HasFuel=true → State=Fueled (1) → Print "Fuel inserted."
          No:  Print "Generator requires fuel." → SetObjective("Find Fuel")
      case Fueled (1):
        CachedInteractor = Interactor
        Print "Generator starting..."
        SetTimerbyFunctionName FinishGeneratorStart (2.0s)

FinishGeneratorStart
  → GeneratorState = Running (2)
  → PowerRestored = true
  → Call OnPowerRestored (dispatcher)
  → Print "Power restored."
  → BPC_Objective.CompleteObjective (CachedInteractor)
```

---

# Power / World Response

```text
BP_PowerManager BeginPlay
  → GetAllActorsOfClass(BP_Generator)
  → Bind OnPowerRestored → HandlePowerRestored
  → Cache BoundGenerator / BoundGeneratorActor

OnPowerRestored (or Tick sees PowerRestored && !HasHandledPower)
  → HandlePowerRestored
  → if !HasHandledPower:
      HasHandledPower = true
      For each class:
        EmergencyLight / PoweredDoor / PowerAmbientFeedback /
        VentilationUnit / PASpeaker / DistantActivityHint
          → OnPowerRestored()
      BPC_Objective.CompleteObjective
      BPC_Objective.SetObjective("Proceed through the powered security door.")
```

---

# Objectives

```text
Caller (pickup / note / generator / PowerManager)
  → BPC_Objective.SetObjective(NewObjective)
  → CurrentObjective = NewObjective
  → ShowObjectiveUI("OBJECTIVE UPDATED", NewObjective)
  → Create WBP_Objective → Setup → AddToViewport
  → Print [PE009] Objective set

CompleteObjective
  → (complete / clear display path as implemented on component)
```

---

# Notes

```text
BP_NotePickup EventInteract(Interactor)
  → Get BPC_Objective on Interactor
  → CreateWidget WBP_NoteReader (PlayerController 0)
  → SetupNote(NoteTitle, NoteBody)
  → AddToViewport
  → if !bCollected:
      bCollected = true
      Print [PE008] Note displayed
      SetObjective("Locate the Facility Key")
```

---

# Flashlight (grant + toggle)

```text
BP_FlashlightPickup Interact
  → BPC_Flashlight.GiveFlashlight
  → SetObjective("Read the maintenance log")
  → DestroyActor

IA_Flashlight Started
  → BPC_Flashlight.ToggleFlashlight
  → if bHasFlashlight: bIsOn = !bIsOn → ApplyLightState
```

---

# Related

- `GameplayFlow.md` — Mermaid overview  
- `BlueprintDependencyMap.md` — static deps  
- `BugHistory.md` — PE-013C input failures  
