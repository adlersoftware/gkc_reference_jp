import json
import os

TYPES = r"D:\dev\gkc_ref\build\types.json"
ROOT = r"D:\dev\Unity\GKC AI\Assets\Game Kit Controller\Scripts"
OUT = r"D:\dev\gkc_ref\build\ai_manifest.json"
NOTES = r"D:\dev\gkc_ref\build\notes"

GROUPS = [
    ("a1", [("findObjectivesSystem", None, None)]),
    ("a2", [("AINavMesh", None, None), ("AIPatrolSystem", None, None), ("AIWayPointPatrol", None, None),
            ("AIAroundManager", None, None), ("changeAIAttackModeByDistance", None, None),
            ("simpleAIAction", None, None), ("handleVehicleAIBehavior", None, None),
            ("AINavMeshMoveInfo", None, None)]),
    ("a3", [("AIFireWeaponsSystemBrain", None, None), ("AICloseCombatSystemBrain", None, None),
            ("AIMeleeCombatSystemBrain", None, None)]),
    ("a4", [("AIBehaviorInfo", None, None), ("AIPowersSystemBrain", None, None),
            ("AIAbilitiesSystemBrain", None, None), ("AITurnBasedCombatSystemBrain", None, None)]),
    ("a5", [("characterFactionManager", None, None), ("friendListManager", None, None),
            ("factionSystem", None, None), ("manageAITarget", None, None), ("AITurret", None, None),
            ("fieldOfViewMeshSystem", None, None), ("enemyLaser", None, None),
            ("objectSignalForTargetToAI", None, None)]),
    ("a6", [("AIHidePositionsManager", None, None), ("AIViewTriggerSystem", None, None),
            ("AIWalkToPosition", None, None), ("AIAimRotationManager", None, None),
            ("shootBowSimpleAIAction", None, None), ("shootFireWeaponSimpleAIAction", None, None),
            ("shootPowerSimpleAIAction", None, None), ("useAbilitySimpleAIAction", None, None),
            ("useCustomAbilitySimpleAIAction", None, None), ("characterToReceiveOrders", None, None),
            ("customOrderBehavior", None, None), ("customOrderBehaviorToAttack", None, None),
            ("customOrderBehaviorToFollow", None, None), ("customOrderBehaviorToHide", None, None),
            ("customOrderBehaviorToUseAbility", None, None), ("addPatrolSystemToAI", None, None),
            ("animalAINavmesh", None, None), ("brainwashAIState", None, None),
            ("eventOnTargetDetectedFaction", None, None), ("sleepingStateIconSystem", None, None)]),
]


def pub_methods(t):
    return [m for m in t["Methods"] if "public" in m["Modifiers"] and not m["IsOverride"] and not m["IsStatic"]]


def main():
    types = [t for t in json.load(open(TYPES, encoding="utf-8")) if not t["IsEditor"] and not t["IsNested"]]
    ai = {}
    for t in types:
        if not t["File"].startswith("AI/"):
            continue
        ms = pub_methods(t)
        if not ms:
            continue
        path = os.path.join(ROOT, t["File"].replace("/", os.sep))
        ai[t["Name"]] = {
            "type": t["Name"],
            "file": t["File"],
            "abs": path,
            "methods": [{"sig": m["Signature"], "line": m["Line"]} for m in ms],
        }

    json.dump(ai, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print("types", len(ai), "methods", sum(len(v["methods"]) for v in ai.values()))

    assigned = set()
    for batch, specs in GROUPS:
        payload = []
        for name, _s, _e in specs:
            if name not in ai:
                print("  missing type:", name)
                continue
            assigned.add(name)
            r = ai[name]
            payload.append({"type": name, "file": r["abs"], "methods": r["methods"]})
        path = os.path.join(NOTES, f"input_{batch}.json")
        json.dump(payload, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(batch, sum(len(p["methods"]) for p in payload), "->", path)

    leftover = [n for n in ai if n not in assigned]
    if leftover:
        print("NOT ASSIGNED:", leftover)


if __name__ == "__main__":
    main()
