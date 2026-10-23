# Game Kit Controller 3.77h リファレンスガイド

インストール済みアセット（`Assets/Game Kit Controller/Scripts`、Unity 6000.4.12f1）から自動生成したリファレンスの使い方と、GKC 固有の読み解き方の解説です。

---

## 1. 生成物

| パス | 内容 |
|---|---|
| [`reference/_INDEX.md`](reference/_INDEX.md) | システム（フォルダ）別の全 998 型一覧。まずここから |
| `reference/<システム>/<型名>.md` | 1 型 = 1 ページ。インスペクター設定・公開メソッド・Unity イベント |
| [`PLAYER_REFERENCE.md`](PLAYER_REFERENCE.md) | Player 関連 72 型 / 2,843 メソッド |
| [`REFERENCES.md`](REFERENCES.md) | 全 51 システムの索引。各システム 1 ファイル（`*_REFERENCE.md`） |
| [`INSPECTOR_REFERENCE.md`](INSPECTOR_REFERENCE.md) | インスペクター設定の日本語解説索引（35 システム / 102 コンポーネント / 4,085 項目） |
| `reference/gkc_api.json` | 型名 / 継承 / ファイル / フィールド数 / 公開メソッド数の索引（機械可読） |
| `docs/` | 公式 GitBook のミラー（英語・全 318 ページ） |
| `sources/gkc_3.7_documentation.txt` | 同梱 PDF（112 ページ）のテキスト版 |

規模: **998 ページ / 23,671 個の public フィールド / 13,175 個の public メソッド / 4,268 行のインスペクター項目（160 コンポーネント）**。
うち **711 型 / 11,665 メソッド**に日本語の一行注釈を付けてあります（全 51 システム）。

---

## 2. 前提: GKC の設計

- **1 キャラクター = 1 プレハブ**。コンポーネント同士はインスペクターの参照で接続されており、`GetComponent` で探し回る設計ではありません。
- 中核は 5 つ:
  `playerController`（移動・状態）、`playerCamera`（視点・カメラステート）、`playerWeaponsManager`（武器）、`inventoryManager`（所持品）、`health`（体力）。
- 共通フィールドは `xxxInfo` 基底クラスに置かれます（例: `inventoryManager : inventoryManagerInfo`）。
  リファレンスの表には**継承元のフィールドも含めて**表示しています。
- 設定はほぼすべて **public フィールド**。実行中に変える場合は、直接代入ではなく `setXxx` / `enableOrDisableXxx` を使ってください（内部キャッシュやイベントが更新されません）。
- イベントは **`useEventXxx`（有効フラグ）+ `eventXxx`（UnityEvent）** のペア。購読する前にフラグをオンにする必要があります。

---

## 3. インスペクター表の読み方

各ページの「インスペクター設定」は、実際のインスペクターの並びを再現しています。

| 列 | 意味 |
|---|---|
| ラベル | インスペクターに**実際に表示される名前**（カスタムエディタの `GUIContent`） |
| フィールド | C# のフィールド名。スクリプト・UnityEvent から触るときはこちら |
| 型 | 宣言型。`GameObject`/`Transform` はシーン参照、`UnityEvent` はインスペクターで登録、`enum` はドロップダウン |
| 既定値 | 宣言時の初期化子。`–` は未初期化（= 0 / false / null） |
| 補足 | **日本語の説明**、`[Tooltip]`、`[Range]`、`[TextArea]`、そして**表示条件** |

「補足」列の先頭は、コードの使われ方から書いた日本語の説明です（35 システム / 102 コンポーネント / 4,085 項目）。一覧は [`INSPECTOR_REFERENCE.md`](INSPECTOR_REFERENCE.md) にあります。

**表示条件**は、そのチェックがオンのときだけ表示される項目です。

```
| Inventory Slot Amount | `inventorySlotAmount` | `int` | – | 表示条件: `infiniteSlots` がオフのとき |
```

例（説明 + 条件）:

```
| Animation Name | `animationName` | `string` | – | 開閉に使うAnimationのクリップ名。 / 表示条件: `movementType.enumValueIndex == 2` |
```

`showAllSettings` / `showXxxSettings` は折りたたみ用トグルです。インスペクターで **Show All Settings** をオンにすると全項目が出ます。

セクション名（`### Main Settings` など）は、エディタ側の `GUILayout.BeginVertical("Main Settings", "window")` に対応します。

### フィールド名の頻出語（意味の手がかり）

| 語 | 意味 |
|---|---|
| `useXxx` / `xxxEnabled` | 機能の有効フラグ（オフなら他の関連項目は効かない） |
| `showXxx` | 表示・UI のフラグ |
| `xxxAmount` | 数量（弾数、所持数、体力など） |
| `xxxRate` / `xxxSpeed` / `xxxTime` | 間隔（秒）／速度／待ち時間（秒） |
| `xxxOffset` / `xxxPosition` | 位置補正／基準位置 |
| `xxxPrefab` | 実行時に生成するプレハブ |
| `xxxLayer` / `xxxMask` | レイヤー番号／LayerMask（対象レイヤーのビット指定） |
| `xxxList` / `xxxArray` | 複数登録（順序に意味があることが多い） |
| `xxxSound` / `xxxAudio` | AudioClip / AudioSource |
| `eventXxx` + `useEventXxx` | UnityEvent 本体と、その発火を有効にするフラグ |

型の読み方: `GameObject`・`Transform` はシーン上の参照、`UnityEvent` はインスペクターで登録するコールバック、`enum` はドロップダウン、`List<T>` は可変長の登録リストです。

---

## 4. 公開メソッドの呼び方

基本形:

```csharp
// 同じ GameObject 上のコンポーネント
var health = GetComponent<health>();
health.setShieldState (true);
```

GKC の public メソッドは「**インスペクターの UnityEvent から呼ぶ**」「**他の GKC コンポーネントから呼ぶ**」前提で作られています。

- 戻り値は `void` がほとんど。結果が必要なら `checkXxx()` / `isXxx()` を別途呼びます。
- **呼ばない**: `Awake` / `Start` / `Update` / `OnTriggerEnter` などの Unity コールバック、`override`（各ページ末尾に折りたたみで分離）。
- **オーバーロードに注意**: 引数が多い版は内部処理用。外部からは引数の少ない版を探してください。
- **連打しない**: 内部でコルーチンやアニメーション待ちがあるため、`setXxx` を毎フレーム呼ぶと状態が壊れます。必要なら `checkIfWeaponStateIsBusy()` のようなガードを使います。

### UnityEvent の購読

```csharp
var health = player.GetComponent<health>();
health.useEventOnDamageEnabled = true;   // インスペクターのフラグをオン
health.eventOnDamage.AddListener (OnPlayerDamaged);
```

`useEventXxx` が false のままだと `eventXxx` は発火しません（ページの「Unity イベント」表に一覧があります）。

---

## 5. 実例（ソースで確認済みのシグネチャ）

| 目的 | コンポーネント | 呼び出し |
|---|---|---|
| ダメージを与える | `health` | `setDamage (damageAmount, fromDirection, damagePosition, attacker, projectile, damageConstant, searchClosestWeakSpot, ignoreShield, ignoreDamageInScreen, damageCanBeBlocked, canActivateReactionSystemTemporally, damageReactionID, damageTypeID)`（13 引数。簡易には `setDamageOrHealthTargetWithDelay(wait, value, typeId)`） |
| 即死させる | `health` | `killCharacter()` |
| 蘇生 | `health` | `resurrect()` |
| シールド ON/OFF | `health` | `setShieldState (bool state)` |
| インベントリ開閉 | `inventoryManager` | `openOrCloseInventory (bool state)` |
| アイテム追加 | `inventoryManager` | `addObjectToInventory (inventoryInfo objectToAdd, int amountToTake, int index)` |
| 名前指定で装備 | `inventoryManager` | `equipObjectByName (string objectName)` |
| 名前指定で使用 | `inventoryManager` | `useInventoryObjectByName (string objectName, int amountToUse)` |
| 武器を選択 | `playerWeaponsManager` | `selectWeaponByName (string weaponName, bool drawSelectedWeapon)` |
| 武器を装備 | `playerWeaponsManager` | `equipWeapon (string weaponName, bool initializingInventory, bool equippingDualWeapon, string rightWeaponName, string lefWeaponName)` |
| 武器を外す | `playerWeaponsManager` | `unequipWeapon (string weaponName, bool unequippingDualWeapon, bool equipSingleWeaponDirectlyIfUsed)` |
| 一人称/三人称切替 | `playerCamera` | `changeCameraView()` |
| カメラステート変更 | `playerCamera` | `setCameraState (string stateName)` |
| 移動入力を外部から上書き | `playerController` | `setCustomAxisValues (Vector2 newValue)` |

引数の意味はフィールド名から読み取れます（例: `ignoreShield` = シールドを無視するか）。数値の単位・推奨値はソースとデモシーンで確認してください。

---

## 6. 網羅性と限界

- 対象は **インストール済み 3.77h のソース**。公式ドキュメント（`docs/`）は 3.7 世代のため、細部が古い場合があります。
- ソースにコメントがほぼ無い（`///` は全 493,752 行中 127 行）ため、**「説明」列は空のことが多い**です。ラベル・型・既定値・表示条件が実質的な情報源です。
- 表示条件は `if` 文からの推定です。実行時に動的に変わる表示（選択内容によって差し替わる等）までは追えません。
- `[SerializeField]` の private フィールドも public と同様に抽出しています。プロパティ（get/set）は一覧に含めていません（GKC ではほぼ未使用）。
- カスタムエディタを持たない型は、`[Header]` を区切りとして宣言順に並べています。

---

## 7. 探し方

```powershell
# クラス名から探す
Get-ChildItem 'D:\dev\gkc_ref\reference' -Recurse -Filter '*Weapon*.md'

# 用語から探す（日本語は無いので英語で）
Select-String -Path 'D:\dev\gkc_ref\reference\**\*.md' -Pattern 'reload' -List

# 公式ドキュメント側を探す
Select-String -Path 'D:\dev\gkc_ref\docs\**\*.md' -Pattern 'inventory' -List
```

`reference/gkc_api.json` を使えば「フィールド数が多い＝設定項目が多いコンポーネント」を機械的に絞り込めます。

---

## 8. 再生成

```powershell
# 1. C# ソースから型情報を抽出（Roslyn）
dotnet run --project 'D:\dev\gkc_ref\tools\GkcExtract\GkcExtract.csproj' -c Release -- `
  'D:\dev\Unity\GKC AI\Assets\Game Kit Controller\Scripts' 'D:\dev\gkc_ref\build\types.json'

# 2. カスタムエディタからインスペクター構成を抽出
python 'D:\dev\gkc_ref\tools\parse_editors.py'

# 3. Markdown を生成
python 'D:\dev\gkc_ref\tools\generate_reference.py'
```

GKC を更新したらこの 3 ステップを流し直せば、リファレンスも追随します。

---

## 9. メソッド注釈（全 51 システム）

実装を読んで付けた日本語の一行解説を、**GKC の全 51 システム・711 型・11,665 メソッド**に用意しています（欠落 0）。

入口は [`REFERENCES.md`](REFERENCES.md) です。システムごとに 1 ファイル（`*_REFERENCE.md`）があり、型の一覧から各コンポーネントページへ移動できます。

| 規模の大きいシステム（例） | 型 | メソッド | ファイル |
|---|---|---|---|
| Weapons | 52 | 1,547 | [`WEAPONS_REFERENCE.md`](WEAPONS_REFERENCE.md) |
| Player（＋camera/weapons/inventory/health） | 68 | 1,519 | [`PLAYER_REFERENCE.md`](PLAYER_REFERENCE.md) |
| AI | 43 | 817 | [`AI_REFERENCE.md`](AI_REFERENCE.md) |
| Inventory | 26 | 629 | [`INVENTORY_REFERENCE.md`](INVENTORY_REFERENCE.md) |
| Vehicles | 30 | 623 | [`VEHICLES_REFERENCE.md`](VEHICLES_REFERENCE.md) |
| Camera | 27 | 606 | [`CAMERA_REFERENCE.md`](CAMERA_REFERENCE.md) |
| Grab Objects | 15 | 541 | [`GRAB_OBJECTS_REFERENCE.md`](GRAB_OBJECTS_REFERENCE.md) |
| Others | 89 | 470 | [`OTHERS_REFERENCE.md`](OTHERS_REFERENCE.md) |
| Health | 16 | 407 | [`HEALTH_REFERENCE.md`](HEALTH_REFERENCE.md) |
| Abilities System | 31 | 382 | [`ABILITIES_REFERENCE.md`](ABILITIES_REFERENCE.md) |

一覧は [`REFERENCES.md`](REFERENCES.md) に全 51 システム分あります。

- 注釈は `notes/method_notes.json` に分離してあり、生成時に各コンポーネントページの「公開メソッド」表へ自動で差し込まれます
- 記法:
  - 「`xxx` を設定するだけ。」= 内部処理を伴わないセッター／ゲッター
  - コルーチン開始、イベント発火、アニメーション待ち、UI 更新を伴う場合はその旨を明記
  - 引数の意味が名前から自明でない場合のみ言及（例: `addObjectToInventory` の `index = -1` は「量 0 の最初の空きスロット」）
  - 空実装は「本体が空で何もしない」と明記（GKC には空の virtual や未使用引数が多数あります）
- 限界: コードから読み取れる挙動のみ。特定条件下でのみ走る分岐や、Inspector 側の設定意図までは踏み込んでいません。

注釈だけを引きたいとき:

```powershell
Select-String -Path 'D:\dev\gkc_ref\reference\Player\*.md' -Pattern '装備' -List
Select-String -Path 'D:\dev\gkc_ref\reference\AI\*.md' -Pattern 'NavMesh' -List
Select-String -Path 'D:\dev\gkc_ref\reference\Event System\*.md' -Pattern 'イベント' -List
```
