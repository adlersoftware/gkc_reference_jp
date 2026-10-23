# Weapons コンポーネント メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Weapons/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **52 型 / 1,547 メソッド**
- 注釈付き: **1,547 メソッド**（100%）
- 生成元: 各 `.cs` の実装。説明はコードの挙動のみに基づきます。

装備の流れは「`playerWeaponsManager`（持ち替え・装備）→ `IKWeaponSystem`（武器モデル/IK/アタッチメント）→ `playerWeaponSystem`（弾・リロード・発射）→ `projectileSystem`（弾の飛翔と着弾）」です。

## 武器本体・中核

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`playerWeaponsManager`](reference/Weapons/playerWeaponsManager.md) | プレイヤーの武器（`IKWeaponSystem`）一覧を保持し、抜刀・納刀、照準、射撃、両手武器、リロード、HUD、アタッチメント、耐久値をまとめて管理する MonoBehaviour。入力系メソッドは入力管理から呼ばれる入口で、Editor 系はインスペクタ操作を補助する。 | 551/551 |
| [`IKWeaponSystem`](reference/Weapons/IKWeaponSystem.md) | 武器1丁ごとの設定コンポーネントで、一人称/三人称の武器メッシュ位置、手と肘のIK目標、スウェイ、射撃時のカメラ揺れ、アタッチメント、デュアルウェルト、耐久値、インベントリ用プレハブ生成を保持する。実際の処理は`playerWeaponSystem`(`weaponSystemManager`)や`playerWeaponsManager`へ委譲する部分が多い。 | 232/232 |
| [`playerWeaponSystem`](reference/Weapons/playerWeaponSystem.md) | 個々の武器オブジェクトに付くコンポーネントで、`weaponInfo`(`weaponSettings`)に持つ装弾数・残弾・発射レート・威力・弾・サウンド・耐久値などの設定を保持し、`playerWeaponsManager` と `IKWeaponSystem` への参照を通じて射撃・リロード・HUD・耐久に関わる値を管理する。ここに載るメソッドは他コンポーネントやエディタから設定値を読み書きするための薄いアクセサが中心。 | 209/209 |
| [`simpleWeaponSystem`](reference/Weapons/simpleWeaponSystem.md) | 武器コンポーネントの簡易版。射撃入力、弾の生成と向き、弾薬、リロード、効果音を扱う。 | 48/48 |
| [`bowSystem`](reference/Weapons/bowSystem.md) | 弓専用コンポーネント。構え、矢の装填、引き絞り、発射、矢種切替、空中弾丸時間を制御する。 | 43/43 |
| [`weaponSystem`](reference/Weapons/weaponSystem.md) | IK 付きの一人称/三人称武器の中核。射撃、弾生成、弾薬、HUD、騒音などを管理する。 | 41/41 |
| [`weaponBuilder`](reference/Weapons/weaponBuilder.md) | 武器モデルのパーツを差し替えて新しい武器を組み立てるエディタ向けコンポーネント。名前・アイコン・耐久値などを`playerWeaponSystem`やインベントリへ反映し、使用可能武器プレハブの生成も行う。 | 35/35 |
| [`weaponAnimatorSystem`](reference/Weapons/weaponAnimatorSystem.md) | 武器の一人称アニメーターの状態を管理し、待機・歩き・走り・射撃・リロード・エイム・抜刀・納刀・近接の各アニメを`CrossFadeInFixedTime`で切り替えるコンポーネント。 | 20/20 |
| [`armorSurfaceSystem`](reference/Weapons/armorSurfaceSystem.md) | 装甲サーフェスとして、当たった弾を蓄積して持ち主へ跳ね返すコンポーネント。装甲の有効状態・耐久値・優先度・当たり判定サイズを管理する。 | 17/17 |
| [`weaponListManager`](reference/Weapons/weaponListManager.md) | 武器ホイールUIを管理し、スロットの表示・武器選択・二丁持ち・ポーズやタイムスケール連携を扱う。 | 14/14 |
| [`weaponTransformInfoSystem`](reference/Weapons/weaponTransformInfoSystem.md) | 武器の保持・照準位置をTransformリストとして保存し、貼り付けや位置調整を行うエディタ補助システム。 | 14/14 |
| [`bowHolderSystem`](reference/Weapons/bowHolderSystem.md) | 弓の装着位置を持ち、矢の装填・射撃・照準開始終了などのタイミングでUnityEventを発火するハブ。 | 8/8 |
| [`weaponObjectInfo`](reference/Weapons/weaponObjectInfo.md) | 武器情報の取得口を提供する基底クラスで、各メソッドは既定値を返すか空のまま。 | 8/8 |
| [`arrowManager`](reference/Weapons/arrowManager.md) | 弓の矢をインベントリの個数と連動させ、HUDの矢パネル・個数・種類アイコンを更新する管理クラス。 | 6/6 |
| [`fakeProjectileTrailSystem`](reference/Weapons/fakeProjectileTrailSystem.md) | 実弾を使わず軌跡だけを目標点まで動かして見せるダミー投射物。時間切れや軌跡の消滅で破棄または非アクティブ化する。 | 6/6 |
| [`simpleSniperSightSystem`](reference/Weapons/simpleSniperSightSystem.md) | スナイパーサイト表示時にカメラ状態とFOVを切り替え、解除時は元のカメラ状態へ戻すシステム。 | 4/4 |
| [`throwGrenadeSystem`](reference/Weapons/throwGrenadeSystem.md) | 投擲グレナードの所持数をHUDへ表示し、投擲開始と確定の入力でイベントを発火するシステム。 | 4/4 |
| [`addGrenadeToThrowAwayFromCharacter`](reference/Weapons/addGrenadeToThrowAwayFromCharacter.md) | 投擲グレナードをプレイヤーのアビリティ所持数へ足し引きする補助コンポーネント。確定時は投射物を投げられる状態へ戻す。 | 3/3 |
| [`dynamicReticleSystem`](reference/Weapons/dynamicReticleSystem.md) | 移動・走り・視点回転・射撃・空中などに応じて照準の大きさを変え、武器の拡散値へ反映するシステム。 | 3/3 |
| [`projectileImpactSystem`](reference/Weapons/projectileImpactSystem.md) | 投射物の着弾地点に音とデカールを出し、一定時間後の破棄やプール返却をまとめて行う小さなシステム。 | 3/3 |
| [`projectilesOnCharacterBodyManager`](reference/Weapons/projectilesOnCharacterBodyManager.md) | キャラの体に刺さった投射物を一定時間後に1本ずつ消していく管理コンポーネント。 | 2/2 |
| [`weaponShellSystem`](reference/Weapons/weaponShellSystem.md) | 排出される薬莢の初速・ランダム回転・衝突無視・再生音を設定するコンポーネント。 | 2/2 |
| [`IKWeaponInfo`](reference/Weapons/IKWeaponInfo.md) | 近接武器のIKや攻撃時サーフェス音を保持する情報クラス。音は`InitializeAudioElements`で`AudioElement`へ複写する。 | 1/1 |
| [`weaponAmmoUsingPlayerStat`](reference/Weapons/weaponAmmoUsingPlayerStat.md) | 射撃時に武器弾薬の代わりにプレイヤーステータスを消費する小さなブリッジ。 | 1/1 |
| [`weaponInfo`](reference/Weapons/weaponInfo.md) | 武器1種の名前・モデル・弾薬・エフェクト・音・イベントなどを保持する中心的な情報クラス。 | 1/1 |
| [`weaponPartstToRemoveOnPickupCreation`](reference/Weapons/weaponPartstToRemoveOnPickupCreation.md) | 拾い物用の武器モデルを作る際に、不要なパーツを削除するための小さなコンポーネント。 | 1/1 |

## アタッチメント（`Weapons/Attachments/`）

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`weaponAttachmentSystem`](reference/Weapons/weaponAttachmentSystem.md) | 武器に装着するアタッチメントの有効・選択状態と、そのUIアイコン／スロットを管理するコンポーネント。編集メニューの開閉に合わせてカメラ・IK・HUDを切り替える。 | 35/35 |
| [`laserAttachment`](reference/Weapons/laserAttachment.md) | 武器に付けるレーザー照準アタッチメント。カメラ前方へレイを飛ばし、レーザーラインと着弾ドットを描画する。 | 2/2 |
| [`laserDotOnScreenSystem`](reference/Weapons/laserDotOnScreenSystem.md) | レーザーの着弾点を画面座標へ変換し、HUDのドットアイコンとして表示するシステム。 | 2/2 |
| [`attachmentInfo`](reference/Weapons/attachmentInfo.md) | 武器アタッチメント1種の名前・スロット・イベント・選択音をまとめた情報クラス。 | 1/1 |

## 特殊武器ビヘイビア（`Weapons/New Weapon Behaviors/`）

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`gravityGun`](reference/Weapons/gravityGun.md) | カメラ前方のレイキャストで掴めるオブジェクトを検出し、`Rigidbody`の重力や回転固定を切り替えて保持・投擲・重力変更を行う武器コンポーネント。 | 29/29 |
| [`surfaceToSlice`](reference/Weapons/surfaceToSlice.md) | 切断可能なサーフェスとして、切断可否・回転数制限・断面マテリアル・切断方向の判定・遅延破棄などを保持し、切断イベントを発火するコンポーネント。 | 25/25 |
| [`smartphoneDevice`](reference/Weapons/smartphoneDevice.md) | 武器として持つスマートフォンを表現し、画面・カメラ・フラッシュ・ズームを制御するコンポーネント。写真撮影、キャプチャ保存、撮影対象イベント、ズーム更新コルーチンを扱う。 | 18/18 |
| [`healerWeapon`](reference/Weapons/healerWeapon.md) | 回復・ダメージ・燃料やエネルギーの補充を切り替えて使う多機能武器。レイキャストした対象へ効果を適用し、設定に応じて弾を消費または回収する。 | 13/13 |
| [`flashlight`](reference/Weapons/flashlight.md) | 武器に付く懐中電灯で、残弾を電池として消費し、ライト・メッシュ・HUD表示・効果音を切り替える。 | 12/12 |
| [`attrackObjectsSystem`](reference/Weapons/attrackObjectsSystem.md) | 照準方向のオブジェクトを引き寄せて保持し、ため撃ちで投げる吸引武器の挙動。掴んだ物のタグ・レイヤー・重力を退避して復元する。 | 11/11 |
| [`sliceObject`](reference/Weapons/sliceObject.md) | 近接武器などに付け、トリガー内の物体を任意平面でスライスしたりダメージを与えたりする挙動。対象の`surfaceToSlice`設定に従う。 | 9/9 |
| [`dragObjectSystem`](reference/Weapons/dragObjectSystem.md) | 掴んだ物体をプレイヤー前方の位置へ追従させ、距離が離れるとイベントを出す運搬用システム。 | 8/8 |
| [`simpleChainSaw`](reference/Weapons/simpleChainSaw.md) | チェーンソーの起動状態と燃料消費、ピボットの手動・自動回転を扱う武器挙動。 | 7/7 |
| [`vacuumGun`](reference/Weapons/vacuumGun.md) | カメラ前方のオブジェクトを吸い寄せて保持し、射出もできる吸引銃の挙動。掴んだ物のレイヤーを退避して復元する。 | 7/7 |
| [`weaponLaser`](reference/Weapons/weaponLaser.md) | 武器から照射するレーザーで、ヒット判定・継続ダメージ・レーザーレシーバーや反射キューブへの接続を扱う挙動。 | 6/6 |
| [`flamethrowerWeapon`](reference/Weapons/flamethrowerWeapon.md) | 火炎放射器の連続噴射を制御し、燃料消費・連続音・開始終了音・パーティクルを切り替える武器挙動。 | 5/5 |
| [`plasmaCutterSystem`](reference/Weapons/plasmaCutterSystem.md) | プラズマカッターのローター角度を手動・自動で回転させ、射撃イベントを発火する武器挙動。 | 5/5 |

## 投射物（`Weapons/Projectiles/`）

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`projectileSystem`](reference/Weapons/projectileSystem.md) | 弾丸やミサイルなど共通の投射物コンポーネント。命中判定、ダメージ、爆発、デカール、プール管理を担当する。 | 50/50 |
| [`plasmaCutterProjectile`](reference/Weapons/plasmaCutterProjectile.md) | プラズマカッター用の投射物で、命中した物体をスライスまたは粉砕し、切断方向へ力を加える。切断回数の上限も持つ。 | 8/8 |
| [`arrowProjectile`](reference/Weapons/arrowProjectile.md) | 矢用の投射物で、着弾面への刺さり・跳ね返り・拾い直しを面の種類ごとに処理する。 | 5/5 |
| [`dissolveProjectile`](reference/Weapons/dissolveProjectile.md) | 着弾した物体へ`dissolveObject`を付け、シェーダーや色を渡して溶かす投射物。溶解完了で自身を破棄する。 | 3/3 |
| [`audioClipBip`](reference/Weapons/audioClipBip.md) | ビープ音を時間経過でピッチと間隔を変えながら鳴らし続け、投射物などの警告音を担うコンポーネント。 | 2/2 |
| [`laserMine`](reference/Weapons/laserMine.md) | レーザービーム式の地雷で、接触回数や時間経過で無効化される投射物の派生クラス。 | 2/2 |
| [`spearProjectile`](reference/Weapons/spearProjectile.md) | 槍の投射物で、着弾時の刺さりや一撃必殺、ラグドールを貫いて運ぶ処理を持つ。 | 2/2 |
| [`taserProjectile`](reference/Weapons/taserProjectile.md) | テーザー用の投射物で、命中したキャラを指定時間だけ気絶させる。 | 2/2 |
| [`projectileInfo`](reference/Weapons/projectileInfo.md) | 投射物の速度・ダメージ・音・切断設定などを保持する情報クラスで、コピー用コンストラクタも持つ。 | 1/1 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- コルーチン（リロード待ち・連射間隔）・アニメータ・IK・イベント発火・弾の生成を伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

