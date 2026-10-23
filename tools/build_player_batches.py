import json, os

MANIFEST = r"D:\dev\gkc_ref\build\player_manifest.json"
OUTDIR = r"D:\dev\gkc_ref\build\notes"

GROUPS = [
    # (batch name, [(type, slice_start, slice_end)])
    ("b1", [("playerController", 0, 155)]),
    ("b2", [("playerController", 155, 310)]),
    ("b3", [("playerController", 310, 460)]),
    ("b4", [("playerController", 460, 611)]),
    ("b5", [("playerComponentsManager", None, None), ("ragdollActivator", None, None),
            ("usingDevicesSystem", None, None), ("IKSystem", None, None)]),
    ("b6", [("customCharacterControllerBase", None, None), ("playerStatesManager", None, None),
            ("freeClimbSystem", None, None), ("upperBodyRotationSystem", None, None),
            ("buildPlayer", None, None), ("slideSystem", None, None),
            ("climbRopeSystem", None, None), ("externalControllerBehavior", None, None)]),
    ("b7", [("quickPlayerModeChangeSystem", None, None), ("jetpackSystem", None, None),
            ("swimSystem", None, None), ("wallSlideJumpSystem", None, None),
            ("ragdollBuilder", None, None), ("customCharacterControllerManager", None, None),
            ("railSystem", None, None), ("walkOnBalanceSystem", None, None),
            ("playerStateSystem", None, None), ("bodyMountPointsSystem", None, None),
            ("flySystem", None, None), ("wallRunningSystem", None, None),
            ("genericRagdollBuilder", None, None), ("multipleInteractionSystem", None, None),
            ("handsOnMeleeWeaponIKSystem", None, None), ("handsOnSurfaceIKSystem", None, None),
            ("characterStateIconSystem", None, None), ("OnAnimatorIKComponent", None, None),
            ("bulletTimeFiringSystem", None, None), ("climbDetectionCollisionSystem", None, None),
            ("paragliderSystem", None, None), ("IKFootSystem", None, None),
            ("characterModelListManager", None, None), ("doubleJumpAnimationTrigger", None, None),
            ("adjustCharacterHeightSystem", None, None), ("freeFallCharacterActivator", None, None),
            ("characterPropertiesSystem", None, None), ("remotePlayerNavmeshOverride", None, None),
            ("freeClimbZoneSystem", None, None), ("externalControllerBehaviorManager", None, None),
            ("remotePlayerNavmeshOverrideSystem", None, None), ("playerSphereModeSystem", None, None),
            ("rollOnLandingSystem", None, None), ("AIMountManager", None, None),
            ("customCharacterControllerBaseBuilder", None, None), ("characterStateAffectedInfo", None, None),
            ("playerIdleSystem", None, None), ("spriteAnimatorSystem", None, None),
            ("characterModelElementInfo", None, None), ("AddPlayerSpawned", None, None),
            ("climbRopeTriggerMatchSystem", None, None), ("climbRopeTriggerSystem", None, None),
            ("portableClimbRopeTriggerSystem", None, None), ("portableWalkOnBalanceTriggerSystem", None, None),
            ("railTriggerSystem", None, None), ("simpleWaypointSystem", None, None),
            ("slideZoneSystem", None, None), ("swimTriggerSystem", None, None),
            ("walkOnBalanceTriggerSystem", None, None), ("wallSlideJumpZoneSystem", None, None),
            ("setCustomCharacterStateTriggerSystem", None, None), ("spiderCharacterController", None, None),
            ("wolfCharacterController", None, None), ("setCharacterAffectedState", None, None),
            ("stairAdherenceSystem", None, None)]),
]


def main():
    manifest = {r["type"]: r for r in json.load(open(MANIFEST, encoding="utf-8"))}
    os.makedirs(OUTDIR, exist_ok=True)

    for batch, specs in GROUPS:
        payload = []
        for type_name, start, end in specs:
            r = manifest[type_name]
            methods = r["methods"]
            if start is not None:
                methods = methods[start:end]
            payload.append({
                "type": type_name,
                "file": r["abs"],
                "methods": [{"sig": m["sig"], "line": m["line"]} for m in methods],
            })
        path = os.path.join(OUTDIR, f"input_{batch}.json")
        json.dump(payload, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        total = sum(len(p["methods"]) for p in payload)
        print(batch, "types", len(payload), "methods", total, "->", path)


if __name__ == "__main__":
    main()
