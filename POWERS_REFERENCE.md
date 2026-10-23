# Powers メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Powers/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **21 型 / 279 メソッド**
- 注釈付き: **279 メソッド**（100%）
- 生成元: 各 `.cs` の実装。テレキネシス、時間操作、重力操作などの特殊能力。

## New Powers Behaviors

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`pushObjectsPower`](reference/Powers/pushObjectsPower.md) | 周囲のオブジェクトを中心から押し出すパワー。範囲内の`Rigidbody`へ力を加え、ダメージや遠隔イベントも任意で行う。 | 13/13 |
| [`joinObjectsPower`](reference/Powers/joinObjectsPower.md) | 2つのオブジェクトを互いに引き寄せるパワー。距離に応じた力を加え、衝突すると解除する。 | 4/4 |
| [`changeGlobalGravityPower`](reference/Powers/changeGlobalGravityPower.md) | カメラ前方の面の法線に合わせて、レベル全体の重力方向を変えるパワー。 | 2/2 |
| [`deviceToControlAtDistance`](reference/Powers/deviceToControlAtDistance.md) | 遠隔操作パワー用に、実際に操作するデバイスを指定する小さなコンポーネント。 | 2/2 |
| [`changeObjectsPositionPower`](reference/Powers/changeObjectsPositionPower.md) | 狙ったオブジェクトとプレイヤーの位置を入れ替えるパワー。 | 1/1 |
| [`useDevicesAtDistancePower`](reference/Powers/useDevicesAtDistancePower.md) | 離れた場所からデバイスやスイッチ、拾得物を使用するパワー。 | 1/1 |

## New Projectiles Behaviors

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`removeGravityFromCharactersProjectile`](reference/Powers/removeGravityFromCharactersProjectile.md) | 着弾地点の範囲内のキャラから、重力を一時的に外す弾。 | 2/2 |
| [`brainwashAIProjectile`](reference/Powers/brainwashAIProjectile.md) | `projectileSystem`を継承した弾で、命中したキャラクターを指定陣営・タグ・名前へ洗脳し、プレイヤーをパートナーに設定できる。 | 1/1 |

## （直下）

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`otherPowers`](reference/Powers/otherPowers.md) | プレイヤーの特殊パワー（念力・発射・重力・時間など）を管理するコンポーネント。パワー選択や照準/フリーファイア、発射物の生成と放物線・追尾、エネルギー消費と回復、HUD・IK・カメラ連携を担う。 | 115/115 |
| [`hitCombat`](reference/Powers/hitCombat.md) | 近接攻撃の当たり判定コンポーネント。手足のトリガーで相手を検出し、ダメージ・押し出し・力を適用する。 | 51/51 |
| [`powersListManager`](reference/Powers/powersListManager.md) | パワーのホイール選択とスロット編集を行うUI管理コンポーネント。割当・アイコン表示・ポーズメニュー連携を担当する。 | 20/20 |
| [`gravityWallRunSystem`](reference/Powers/gravityWallRunSystem.md) | 壁走りシステム。ランボタン長押しで重力方向を壁面へ回し、マテリアル・速度・イベントを切り替える。 | 19/19 |
| [`timeBullet`](reference/Powers/timeBullet.md) | バレットタイム（時間スローの）管理。`Time.timeScale`を書き換え、持続時間や音のピッチも扱う。 | 18/18 |
| [`launchedObjects`](reference/Powers/launchedObjects.md) | 発射されたオブジェクトに付与され、衝突相手へ速度由来のダメージや遠隔イベントを与えるコンポーネント。 | 8/8 |
| [`slowObject`](reference/Powers/slowObject.md) | オブジェクトを一定時間スローモーションにする状態。色変更コンポーネントを付与し、開始/終了イベントを持つ。 | 7/7 |
| [`gravityBootsSystem`](reference/Powers/gravityBootsSystem.md) | 重力ブーツ。壁面など任意の表面に吸着して歩けるよう、法線方向へ重力と向きを回転させる。 | 6/6 |
| [`blackHoleProjectile`](reference/Powers/blackHoleProjectile.md) | 黒穴として機能する特殊弾。範囲内の`Rigidbody`を引き込み、終了時に爆発させて放出する。 | 3/3 |
| [`powersAndAbilitiesSystem`](reference/Powers/powersAndAbilitiesSystem.md) | パワー名と有効/無効イベントを対応付ける汎用システム。名前を指定してイベントを呼び出す。 | 3/3 |
| [`gravityWallRunTriggerSystem`](reference/Powers/gravityWallRunTriggerSystem.md) | `tagToCheck`のプレイヤーがトリガーに出入りすると、その`gravityWallRunSystem`の壁走りやアニメ速度を外部から切り替える。 | 1/1 |
| [`nanoBlade`](reference/Powers/nanoBlade.md) | `projectileSystem`を継承した投擲弾で、命中したオブジェクトや最寄りのラグドールボーンに弾を固定し、ダメージと衝撃力を与える。 | 1/1 |
| [`slowObjectsColor`](reference/Powers/slowObjectsColor.md) | `slowObject`から開始され、対象の速度を低下させながらレンダラーを`slowColor`へ補間し、時間経過で元の色と速度に戻して自己破棄する。 | 1/1 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- 状態遷移・イベント発火・UI 更新・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

