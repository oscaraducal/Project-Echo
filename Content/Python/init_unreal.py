# ProjectEcho Python startup — one-shot PE-012 runner when flag present
import unreal
import os

_FLAG = r"C:\Users\oscar\Documents\Unreal Projects\ProjectEcho\Saved\PE012_run.flag"
_SCRIPT = r"C:\Users\oscar\Documents\Unreal Projects\ProjectEcho\Saved\PE012_complete_safe.py"
_STATUS = r"C:\Users\oscar\Documents\Unreal Projects\ProjectEcho\Saved\PE012_status.txt"
_TICK_HANDLE = None
_FRAMES = 0


def _append(msg: str) -> None:
    try:
        with open(_STATUS, "a", encoding="utf-8") as f:
            f.write(msg + "\n")
    except Exception:
        pass
    unreal.log(msg)


def _on_tick(_delta: float) -> None:
    global _TICK_HANDLE, _FRAMES
    _FRAMES += 1
    # Wait for editor subsystems / asset registry to settle
    if _FRAMES < 120:
        return
    if _TICK_HANDLE is not None:
        try:
            unreal.unregister_slate_post_tick_callback(_TICK_HANDLE)
        except Exception:
            pass
        _TICK_HANDLE = None
    try:
        _append("[PE012] startup hook executing complete script")
        with open(_SCRIPT, "r", encoding="utf-8") as f:
            code = f.read()
        # Execute in a fresh globals dict with unreal available
        g = {"unreal": unreal, "__name__": "__pe012_main__"}
        exec(compile(code, _SCRIPT, "exec"), g, g)
        _append("[PE012] startup hook finished")
    except Exception as e:
        _append(f"[PE012] startup hook FAILED: {e}")
        unreal.log_error(f"[PE012] startup hook FAILED: {e}")


def _maybe_schedule_pe012() -> None:
    global _TICK_HANDLE
    if not os.path.exists(_FLAG):
        return
    try:
        os.remove(_FLAG)
    except Exception as e:
        unreal.log_warning(f"[PE012] could not remove flag: {e}")
        return
    try:
        with open(_STATUS, "w", encoding="utf-8") as f:
            f.write("[PE012] flag detected — scheduling deferred run\n")
    except Exception:
        pass
    _TICK_HANDLE = unreal.register_slate_post_tick_callback(_on_tick)
    unreal.log("[PE012] scheduled deferred PE-012 completion")


_maybe_schedule_pe012()
