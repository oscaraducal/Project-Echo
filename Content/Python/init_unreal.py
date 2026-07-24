# ProjectEcho Python startup — one-shot deferred runners when flag present
import unreal
import os

_SAVED = r"C:\Users\oscar\Documents\Unreal Projects\ProjectEcho\Saved"
_TICK_HANDLE = None
_FRAMES = 0
_PENDING = None  # (script_path, status_path, tag)


def _append(status_path: str, msg: str) -> None:
    try:
        with open(status_path, "a", encoding="utf-8") as f:
            f.write(msg + "\n")
    except Exception:
        pass
    unreal.log(msg)


def _on_tick(_delta: float) -> None:
    global _TICK_HANDLE, _FRAMES, _PENDING
    _FRAMES += 1
    # Wait for editor subsystems / asset registry to settle
    if _FRAMES < 30:
        return
    script_path, status_path, tag = _PENDING
    if _TICK_HANDLE is not None:
        try:
            unreal.unregister_slate_post_tick_callback(_TICK_HANDLE)
        except Exception:
            pass
        _TICK_HANDLE = None
    try:
        _append(status_path, f"[{tag}] startup hook executing script")
        with open(script_path, "r", encoding="utf-8") as f:
            code = f.read()
        g = {"unreal": unreal, "__name__": f"__{tag}_main__"}
        exec(compile(code, script_path, "exec"), g, g)
        _append(status_path, f"[{tag}] startup hook finished")
    except Exception as e:
        _append(status_path, f"[{tag}] startup hook FAILED: {e}")
        unreal.log_error(f"[{tag}] startup hook FAILED: {e}")
    _PENDING = None


def _schedule(flag_name: str, script_name: str, status_name: str, tag: str) -> bool:
    global _TICK_HANDLE, _FRAMES, _PENDING
    flag = os.path.join(_SAVED, flag_name)
    if not os.path.exists(flag):
        return False
    try:
        os.remove(flag)
    except Exception as e:
        unreal.log_warning(f"[{tag}] could not remove flag: {e}")
        return False
    script_path = os.path.join(_SAVED, script_name)
    status_path = os.path.join(_SAVED, status_name)
    try:
        with open(status_path, "w", encoding="utf-8") as f:
            f.write(f"[{tag}] flag detected — scheduling deferred run\n")
    except Exception:
        pass
    _PENDING = (script_path, status_path, tag)
    _FRAMES = 0
    _TICK_HANDLE = unreal.register_slate_post_tick_callback(_on_tick)
    unreal.log(f"[{tag}] scheduled deferred run")
    return True


# Prefer ASSET-001 if present; otherwise PE-012 legacy flag
if not _schedule("ASSET001_run.flag", "ASSET001_migrate.py", "ASSET001_status.txt", "ASSET-001"):
    _schedule("PE012_run.flag", "PE012_complete_safe.py", "PE012_status.txt", "PE012")
