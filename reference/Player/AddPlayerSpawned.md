# AddPlayerSpawned

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **namespace**: `GameKitController.Player`
- **ソース**: `Player/AddPlayerSpawned.cs:5`

**概要**: 生成されたプレイヤーを `playerCharactersManager` に登録する小さなコンポーネント。`Start` で自身を自動登録する。

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `AddNewPlayerSpawned(GameObject gameObj)` | `gameObj` が null なら自身を使い、プレイヤー管理に登録する。 |
