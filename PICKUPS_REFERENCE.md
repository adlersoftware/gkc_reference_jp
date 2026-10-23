# PickUps メソッドリファレンス

`Assets/Game Kit Controller/Scripts/PickUps/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **16 型 / 123 メソッド**
- 注釈付き: **123 メソッド**（100%）
- 生成元: 各 `.cs` の実装。説明はコードの挙動のみに基づきます。

`pickUpObject` が拾えるオブジェクト本体、`pickupType` が拾った中身の定義、`pickUpManager` がシーン内の拾い物管理、`playerPickupIconManager` / `pickUpsScreenInfo` が UI 表示を担当します。

## 拾い物の中核

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`pickUpObject`](reference/PickUps/pickUpObject.md) | シーン上の拾得物1個を表し、トリガー接触またはボタンで拾得者を判定して`pickupType`経由で取得を実行する。インベントリ追加、HUDアイコン/メッセージ、取得イベント、耐久値、オブジェクト破棄を扱う。 | 44/44 |
| [`pickUpManager`](reference/PickUps/pickUpManager.md) | 拾得物のHUDアイコン登録を一元管理するシングルトン。種類名からテクスチャとプレハブを解決し、IDで全プレイヤーの表示を追加・削除・一時停止する。 | 11/11 |
| [`chestSystem`](reference/PickUps/chestSystem.md) | プレイヤーが近づいて開くと、設定された中身のピックアップを生成して箱の中に並べる宝箱。開閉アニメ、再補充・再開封の待ち時間、施錠と解錠、開閉イベントを管理する。 | 10/10 |
| [`playerPickupIconManager`](reference/PickUps/playerPickupIconManager.md) | プレイヤーごとに拾得物アイコンをHUDへ生成し、`pickUpIconList`で追跡する。表示/非表示、一時停止、画面サイズ更新、`pickUpManager`とのID同期を担う。 | 10/10 |
| [`dropPickUpSystem`](reference/PickUps/dropPickUpSystem.md) | 敵などの位置に、抽選・確率・ランダム内容の設定に従ってピックアップを生成し、爆発力で周囲に散らすシステム。設計図の分解素材ドロップや生成イベントにも対応する。 | 8/8 |
| [`explosiveBarrel`](reference/PickUps/explosiveBarrel.md) | 衝突速度やダメージで爆発する爆発性の樽。範囲ダメージ、爆風、破片生成、フェード削除、遅延爆発を設定でき、プレイヤーが把持している間は衝突爆発を止められる。 | 7/7 |
| [`pickUpsScreenInfo`](reference/PickUps/pickUpsScreenInfo.md) | 拾得した物の名前と数を画面に積み上げ表示し、`durationTimerPerText`経過ごとに古い表示を`Destroy`して位置を詰める。アイコン付きの表示にも対応する。 | 7/7 |
| [`crate`](reference/PickUps/crate.md) | 速度の出た衝突で壊れる木箱。破片の生成・飛散・フェード削除と破壊音を扱い、`canBeBroken` で破壊を抑止できる。 | 4/4 |

## 拾い物の種類

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`pickupType`](reference/PickUps/pickupType.md) | 拾えるオブジェクトの基底クラスで、取得可否の判定、取得確定、取得メッセージ表示、アビリティ解放や設計図追加といった共通処理を持つ。個々の取得挙動はサブクラスが上書きして実装する。 | 14/14 |
| [`weaponPickup`](reference/PickUps/weaponPickup.md) | 武器そのものを拾うピックアップ。`playerWeaponsManager` で所持状況やエイム中・武器切替中かを確認して取得可否を決め、取得・インベントリ保存・メッセージ表示を行う。 | 2/2 |
| [`ammoPickup`](reference/PickUps/ammoPickup.md) | 弾薬用のピックアップ。所持武器や車両武器の弾薬上限を確認して取得量を決め、`AddAmmo` または車両HUDへ加算し、残量があれば再取得イベントを送る。 | 1/1 |
| [`generalPickup`](reference/PickUps/generalPickup.md) | 汎用ピックアップ。インベントリへ保存するか、プレイヤーステータスの加算、リモートイベント、アビリティ解放、設計図追加を直接実行するかを選べる。 | 1/1 |
| [`meleeShieldPickup`](reference/PickUps/meleeShieldPickup.md) | 盾用のピックアップ。`meleeWeaponsGrabbedManager` の設定に応じて装備かインベントリ保存かを切り替え、取得処理とメッセージ表示を行う。 | 1/1 |
| [`meleeWeaponConsumablePickup`](reference/PickUps/meleeWeaponConsumablePickup.md) | 近接武器の消耗品用ピックアップ。インベントリ保存時のみ取得可能とし、取得時はメッセージとサウンドを出してレベルから取り除く。 | 1/1 |
| [`meleeWeaponPickup`](reference/PickUps/meleeWeaponPickup.md) | 近接武器用のピックアップ。インベントリに保存できる場合のみ取得可とし、取得時はメッセージ・サウンド・レベルからの削除を行う。 | 1/1 |
| [`weaponAttachmentPickup`](reference/PickUps/weaponAttachmentPickup.md) | 武器アタッチメント用のピックアップ。インベントリへ保存するか、所持武器へ装着できるかを判定し、取得メッセージとサウンドを出して消える。 | 1/1 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- インベントリ追加・UI アイコン・イベント発火・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

