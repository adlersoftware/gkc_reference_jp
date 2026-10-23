# showGameInfoHud

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/showGameInfoHud.cs:6`

**概要**: HUD要素を親名と要素名で検索して返し、必要ならパネルをプレハブから生成する。

**公式ドキュメント抜粋**（[Show Game Info Hud](../../docs/character-level-components/character/show-game-info-hud.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Hud Elements | `hudElements` | `List<hudElementInfo>` | new List<hudElementInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getHudElement(string parentName, string elementName)` | `parentName`一致の要素群から`elementName`一致の`rectTransform`の`GameObject`を返し、無ければ`null`を返す。 |
| `getHudElements(string parentName, List<string> elementNames)` | `parentName`配下で`elementNames`に含まれる名前の要素を集め、`List<GameObject>`として返す。 |
| `getHudElementParent(string parentName)` | `parentName`一致の親を返し、未生成でプレハブ指定があれば生成してから返す。 |

## 内部型

- `elementType`（enum）
- `hudElementInfo`（class）
- `rectTransformInfo`（class）
