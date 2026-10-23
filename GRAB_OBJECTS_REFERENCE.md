# Grab Objects メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Grab Objects/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **15 型 / 541 メソッド**
- 注釈付き: **541 メソッド**（100%）
- 生成元: 各 `.cs` の実装。物を掴む・運ぶ・投げる・近接攻撃までを担う物理グラブ系。

## （直下）

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`grabbedObjectMeleeAttackSystem`](reference/Grab%20Objects/grabbedObjectMeleeAttackSystem.md) | プレイヤーが把持した近接武器の攻撃・ガード・シールド・投擲・切断を統括するコンポーネント。`grabbedWeaponInfo`の設定に従い、攻撃コルーチン、ダメージトリガー、移動設定、各種イベントを実行する。 | 211/211 |
| [`grabObjects`](reference/Grab%20Objects/grabObjects.md) | `grabObjects`は、プレイヤーが注視した剛体オブジェクトを掴んで保持・運搬・投擲・ドロップさせるプレイヤー側コンポーネント。タグとレイヤの一時退避、重量と筋力の判定、IKやカーソル、透明化、`grabPhysicalObjectSystem`による両手持ちまで制御する。 | 84/84 |
| [`grabPhysicalObjectMeleeAttackSystem`](reference/Grab%20Objects/grabPhysicalObjectMeleeAttackSystem.md) | 近接武器（剣・槍など）の攻撃情報、投擲と返却、防御、耐久値、追加アクション、被弾面のリモートイベントをまとめて管理する武器コンポーネント。`grabPhysicalObjectSystem`と連携し、攻撃リストやトレイル、ダメージ属性を実行時に切り替える。 | 77/77 |
| [`grabPhysicalObjectSystem`](reference/Grab%20Objects/grabPhysicalObjectSystem.md) | 掴める物理オブジェクト側に付き、プレイヤーの`grabObjects`へ検出・掴み・ドロップを通知するコンポーネント。質量やレイヤー、キネマティック、IK/アニメ設定、イベントやリモートイベントを掴み状態に応じて切り替える。 | 56/56 |
| [`objectToPlaceSystem`](reference/Grab%20Objects/objectToPlaceSystem.md) | 配置対象オブジェクト（ケーブル端末など）が配置済み・把持中・他オブジェクト接続中かを保持する。`putObjectSystem` との接続、イベント通知、周囲の配置先探索を仲介する。 | 35/35 |
| [`putObjectSystem`](reference/Grab%20Objects/putObjectSystem.md) | オブジェクトを受け取って配置する側のコンポーネントで、トリガー進入／退出や名前条件で対象を判定する。配置位置への移動、配置／解除イベント、配置数の管理を行う。 | 23/23 |
| [`outlineObjectSystem`](reference/Grab%20Objects/outlineObjectSystem.md) | マテリアルのシェーダー差し替えでアウトラインと透過を制御するコンポーネントで、描画要素と元シェーダーを保存する。表示中のプレイヤーをリスト管理し、解除時に元へ戻す。 | 12/12 |
| [`grabbedObjectState`](reference/Grab%20Objects/grabbedObjectState.md) | オブジェクトが把持されているかを保持する状態コンポーネントで、把持者・無重力室・物理把持の各フラグを管理する。把持／解放時の UnityEvent も持つ。 | 12/12 |
| [`grabObjectsPowerSystem`](reference/Grab%20Objects/grabObjectsPowerSystem.md) | パワーで周囲または注視先のオブジェクトを掴み、ボタン長押しでためた力を加えて投擲するシステム。把持リスト、照準スライダー、投擲イベントを管理する。 | 10/10 |
| [`grabObjectGenericModeMountPointSystem`](reference/Grab%20Objects/grabObjectGenericModeMountPointSystem.md) | ジェネリックモードの把持で使うマウントポイントと参照位置を名前で引くためのデータ保持コンポーネント。既定ポイントとスケール倍率の設定も持つ。 | 6/6 |
| [`grabObjectProperties`](reference/Grab%20Objects/grabObjectProperties.md) | オブジェクト個別の重さ・追加把持距離・投擲用の質量などを保持し、把持／解放イベントを中継するコンポーネント。 | 6/6 |
| [`objectDistributorSystem`](reference/Grab%20Objects/objectDistributorSystem.md) | `objectToSpawn` を配置位置から生成して放出する自販機型のコンポーネント。残数制限、開閉アニメーション、生成／空／開閉イベントを扱う。 | 4/4 |
| [`checkObjectOnTrigger`](reference/Grab%20Objects/checkObjectOnTrigger.md) | トリガー内に入った配置可能オブジェクトをリストで保持し、配置／退出に応じて UnityEvent を発火する判定コンポーネント。 | 2/2 |
| [`grabObjectEventSystem`](reference/Grab%20Objects/grabObjectEventSystem.md) | 把持・解放時に UnityEvent を呼ぶだけの小規模なイベント中継コンポーネント。 | 2/2 |
| [`grabObjectParent`](reference/Grab%20Objects/grabObjectParent.md) | 把持対象の `GameObject` を1つ保持して返すだけの参照用コンポーネント。 | 1/1 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- 状態遷移・イベント発火・UI 更新・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

