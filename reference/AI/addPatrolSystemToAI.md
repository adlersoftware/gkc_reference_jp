# addPatrolSystemToAI

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `AI/addPatrolSystemToAI.cs:5`

**概要**: インスペクタのボタンからAIへ巡回システムや`AIWayPointPatrol`を追加・割り当てするエディタ補助。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main AI Patrol System | `mainAIPatrolSystem` | `AIPatrolSystem` | – | – |
| AI Waypoint Patrol Universal Prefab | `AIWaypointPatrolUniversalPrefab` | `GameObject` | – | – |
| Main AI Waypoint Patrol | `mainAIWaypointPatrol` | `AIWayPointPatrol` | – | – |
| Explanation | `explanation` | `string` | "The button Add Patrol System to AI w… | TextArea (1, 10) |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `enableOrdisablePatrolOnAI(bool state)` | 必要なら`mainAIPatrolSystem`を取得し、巡回の停止と有効状態を`state`に合わせる。 |
| `assignAIWaypointPatrol()` | 既存の`AIWayPointPatrol`を探し（無ければ生成）、AIの`patrolPath`へ設定して巡回を再開する。 |
| `addPatrolSystem()` | プレハブから巡回オブジェクトを生成してAIへ割り当て、設定済みなら警告を出す。 |
