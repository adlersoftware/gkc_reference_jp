# Demo メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Demo/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **8 型 / 20 メソッド**
- 注釈付き: **20 メソッド**（100%）
- 生成元: 各 `.cs` の実装。デモシーン専用の補助スクリプト。

## （直下）

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`moveObject`](reference/Demo/moveObject.md) | `originalPosition`を基準に、`direction`・`speed`・`moveAmount`でコサイン波の往復移動をFixedUpdateで行うデモ用コンポーネント。`useLocalPosition`でローカル座標とワールド座標を切り替える。公開メソッドは移動の有効/無効の切り替えのみ。 | 4/4 |
| [`simpleTurretRobot`](reference/Demo/simpleTurretRobot.md) | 機銃と主砲の`Animation`を`CrossFade`で正転/逆転させ、ウェポンの展開と収納を演出するデモ用コンポーネント。`pressButton`で`activated`を反転して両アニメの再生方向を切り替える。 | 4/4 |
| [`checkCollisionToApplyDamage`](reference/Demo/checkCollisionToApplyDamage.md) | 衝突した相手へ、体力へのダメージ・キル・押し出しを設定に応じて行うデモ用コンポーネント。`damageEnabled`がfalseの間は衝突処理の冒頭でreturnし、何もしない。 | 3/3 |
| [`damageCharacterOnCollision`](reference/Demo/damageCharacterOnCollision.md) | 衝突相手のRigidbodyに力を加え、設定に応じて`applyDamage`経由でダメージやキル、押し出しを行うデモ用コンポーネント。`damageEnabled`がfalseの間は衝突処理を早期returnする。 | 3/3 |
| [`simpleObject`](reference/Demo/simpleObject.md) | `working`がtrueの間、Updateで`mainAnimation`の`animationName`を再生し、再生終了ごとに速度の符号を反転して往復させるデモ用コンポーネント。 | 2/2 |
| [`setLaserRefractions`](reference/Demo/setLaserRefractions.md) | UIスライダーの値から、プレイヤーの`Shield`能力(`playerShieldSystem`)のレーザー屈折上限を変更するデモ用コンポーネント。変更値は同時にテキストへ表示する。 | 2/2 |
| [`setText`](reference/Demo/setText.md) | `Text`/`TextMesh`の文字列を看板メッシュに反映し、プレイヤーがトリガー内にいる間だけ`MeshRenderer`を表示するデモ用コンポーネント。 | 1/1 |
| [`openStructure`](reference/Demo/openStructure.md) | `objectsToFade`のアルファを徐々に変化させ、透明シェーダーとColliderの有効/無効で構造物の出入りを可能にするデモ用コンポーネント。 | 1/1 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- 状態遷移・イベント発火・UI 更新・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

