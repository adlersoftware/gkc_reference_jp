# Character Aspect Customization System メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Character Aspect Customization System/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **5 型 / 60 メソッド**
- 注釈付き: **60 メソッド**（100%）
- 生成元: 各 `.cs` の実装。見た目パーツ（アーマー・服）の差し替え。

## （直下）

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`characterCustomizationManager`](reference/Character%20Aspect%20Customization%20System/characterCustomizationManager.md) | キャラクターの外見を管理する中核コンポーネントで、`characterObjectTypeInfoList`の装備パーツ、`characterAccessoriesTypeInfoList`のアクセサリー、`characterBlendShapeTypeInfoList`のブレンドシェイプを切り替えます。現在装備中の`currentPiecesList`と`currentAccessoriesList`を保持し、テンプレート適用や一人称視点時のメッシュ非表示も扱います。 | 25/25 |
| [`characterAspectCustomizationUISystem`](reference/Character%20Aspect%20Customization%20System/characterAspectCustomizationUISystem.md) | キャラクター作成メニューのUI制御コンポーネントで、ボタン/トグル/スライダーの入力を`characterCustomizationManager`のカスタマイズ処理へ中継します。パネル開閉やカメラ位置、キャラクター回転、マルチキャラクターの切り替えも扱います。 | 24/24 |
| [`characterCustomizationBlendshapesHelper`](reference/Character%20Aspect%20Customization%20System/characterCustomizationBlendshapesHelper.md) | ブレンドシェイプ値とアクセサリー構成を一時的に退避し、別のキャラクターモデルへ復元するための補助コンポーネントです。`characterCustomizationManager`を自動検索し、キャラクターモデルIDの取得と切り替えも提供します。 | 6/6 |
| [`characterCustomizationInventoryHelper`](reference/Character%20Aspect%20Customization%20System/characterCustomizationInventoryHelper.md) | 現在装備中のカスタマイズ要素を`inventoryInfo`としてインベントリ用リストに変換する補助コンポーネントです。フルアーマーセットが完成している場合は`extraInventoryInfoList`から追加アイテムも加えます。 | 4/4 |
| [`armorClothPickup`](reference/Character%20Aspect%20Customization%20System/armorClothPickup.md) | `pickupType`を継承したアーマー/服のピックアップで、プレイヤーの`inventoryCharacterCustomizationSystem`の有無でインベントリ格納可否を判定します。取得時にはメッセージ表示、サウンド再生、レベルからの削除を行います。 | 1/1 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- 状態遷移・イベント発火・UI 更新・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

