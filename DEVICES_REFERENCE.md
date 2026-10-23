# Devices メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Devices/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **38 型 / 336 メソッド**
- 注釈付き: **336 メソッド**（100%）
- 生成元: 各 `.cs` の実装。説明はコードの挙動のみに基づきます。

デバイスは Action System から「調べる／使う」対象になるシーンオブジェクトです。`electronicDevice` が共通の操作窓口、`doorSystem` / `hologramDoor` / `padlockSystem` が扉と鍵、`lockedCameraSystem` が固定カメラ視点を担当します。

## デバイス中核

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`lockedCameraSystem`](reference/Devices/lockedCameraSystem.md) | 固定カメラ（locked camera）のゾーン・カメラ軸・トリガー・ウェイポイントを保持し、`playerCamera` にカメラ切替を指示するコンポーネント。メソッドの大半はエディタ用の要素生成/削除と、全カメラ共通フラグの一括設定。 | 37/37 |
| [`doorSystem`](reference/Devices/doorSystem.md) | 扉パネルの移動/回転/アニメーションによる開閉、施錠、効果音、開閉イベント、マップアイコンを処理する。プレイヤーのトリガーや射撃、ボタンから開閉を呼び出せる。 | 23/23 |
| [`electronicDevice`](reference/Devices/electronicDevice.md) | Action System で使う端末の使用状態を管理し、プレイヤーのトリガー進入/退出、カメラ移動、使用開始/停止イベントを処理する。`usingDevicesSystem` のデバイス一覧への登録・解除も担う。 | 23/23 |
| [`deviceStringAction`](reference/Devices/deviceStringAction.md) | Action System が表示するデバイス名・行動名（`deviceAction`）・アイコン表示状態と、その表示用トランスフォームやフォントサイズを保持する。ほぼ getter/setter のみ。 | 17/17 |
| [`examineObjectSystem`](reference/Devices/examineObjectSystem.md) | オブジェクトをカメラ前に寄せ、回転・ズームで調べるためのデバイス。調べポイント押下の順序判定、メッセージ、イベント、使用終了や無効化を受け持つ。 | 16/16 |
| [`hologramDoor`](reference/Devices/hologramDoor.md) | `doorSystem` の手前に置くホログラム制御で、トリガーへの入退場とタグ判定で扉を開閉する。テキスト・色・透明度・効果音・`eventOnOpen` で施錠／解錠の見た目を演出する。 | 16/16 |
| [`padlockSystem`](reference/Devices/padlockSystem.md) | 数字ホイール式の南京錠で、タッチ・キーボード・マウスホイールの入力から現在のコードを組み立てる。`correctCode` と一致すると解錠して `unlockObject` を呼ぶ。 | 14/14 |
| [`accessTerminal`](reference/Devices/accessTerminal.md) | コード入力式の端末で、画面上のキーやキーボードから桁を入力して `code` と照合する。解錠時は `unlockObject` を呼び、表示色・テキスト・イベント・ハックパネルを切り替える。 | 13/13 |
| [`elevatorSystem`](reference/Devices/elevatorSystem.md) | 階リスト間を移動するエレベータで、内外扉の閉鎖完了を待ってから移動を始める。乗客の親子付け、階ボタン `callElevator`、階の追加削除も管理する。 | 13/13 |
| [`waypointPlatform`](reference/Devices/waypointPlatform.md) | ウェイポイント間を往復・周回する移動プラットフォームで、乗客や車両の親子付け、トリガー検出、ミラー移動、到達イベントを扱う。 | 13/13 |
| [`moveDeviceToCamera`](reference/Devices/moveDeviceToCamera.md) | デバイス本体をプレイヤーカメラの前に引き寄せて観察させるコンポーネント。終了時は元の親・位置・回転へ戻す。 | 11/11 |
| [`simpleSwitch`](reference/Devices/simpleSwitch.md) | 単発/双方向のスイッチ。アニメと効果音を再生し、`UnityEvent`または`SendMessage`で対象オブジェクトを操作する。 | 10/10 |
| [`closetSystem`](reference/Devices/closetSystem.md) | 複数のドア付き収納を管理し、ドア開閉のアニメーション、内部オブジェクトの生成・表示切替、プレイヤーのデバイス一覧更新を行う。 | 9/9 |
| [`hackTerminal`](reference/Devices/hackTerminal.md) | 4方向アイコンの順番当てでデバイスをハッキングする端末。HUD表示、カメラ移動、制限時間、成功/失敗イベントを管理する。 | 9/9 |
| [`waypointPlayerPathSystem`](reference/Devices/waypointPlayerPathSystem.md) | ウェイポイント巡回路。順番制/順不同の到達判定、タイマー、マップアイコン、ライン表示、完了/失敗イベントを管理する。 | 9/9 |
| [`examineObjectSystemPlayerManagement`](reference/Devices/examineObjectSystemPlayerManagement.md) | プレイヤー側の観察入力を現在の観察対象へ中継する管理コンポーネント。ズームと回転リセット、キャンセルを扱う。 | 8/8 |
| [`moveCameraToDevice`](reference/Devices/moveCameraToDevice.md) | デバイス使用時にプレイヤーカメラを`cameraPosition`へ移動し、終了時に元へ戻すコンポーネント。使用中は操作や武器、HUDを停止する。 | 8/8 |
| [`zipline`](reference/Devices/zipline.md) | プレイヤーがぶら下がって移動するジップライン。IK、親子付け、速度制御、接続状態を管理する。 | 7/7 |
| [`computerDevice`](reference/Devices/computerDevice.md) | パスワード入力式の端末。押されたキーを画面のコード文字列へ反映し、Enterで照合して一致時にアンロック状態へ切り替える。 | 6/6 |
| [`securityCamera`](reference/Devices/securityCamera.md) | 監視カメラの首振りとズームを制御する。通常入力と`overrideInputManager`による強制操作の両方に対応する。 | 6/6 |
| [`enemyHackPanel`](reference/Devices/enemyHackPanel.md) | 敵デバイス用のハッキングパネル。ハックの開始・停止を`hackTerminal`へ渡し、成功/失敗のイベントを発火する。 | 5/5 |
| [`interactionObjectMessage`](reference/Devices/interactionObjectMessage.md) | トリガー内のプレイヤーへメッセージを表示するデバイス。任意でカメラ移動、操作停止、開始/終了イベントも行う。 | 4/4 |
| [`laserConnector`](reference/Devices/laserConnector.md) | 偏向されたレーザーを反射先まで伸ばすコネクタ。ヒット先がレシーバーかプリズムかで接続状態を切り替える。 | 4/4 |
| [`oneWayPlatformSystem`](reference/Devices/oneWayPlatformSystem.md) | 一方通行の足場。進入方向やしゃがみ・入力の条件に応じ、プレイヤーとのコリジョンを選択的に無視する。 | 4/4 |
| [`padlockSystemPlayerManagement`](reference/Devices/padlockSystemPlayerManagement.md) | プレイヤー側の南京錠パズル入力を、現在の`padlockSystem`へ中継する管理コンポーネント。 | 4/4 |
| [`securityCameraControl`](reference/Devices/securityCameraControl.md) | 監視カメラ用の操作UI。ジョイスティックとズームボタンへのタッチ/マウス入力、プレイヤー入力をカメラ回転へ変換する。 | 4/4 |
| [`teleportationPlatform`](reference/Devices/teleportationPlatform.md) | 触れたオブジェクトを対向する転送先プラットフォームへ送る。位置・回転・重力方向の調整とイベント発火を行う。 | 4/4 |
| [`laser`](reference/Devices/laser.md) | レーザービームの見た目を制御する基底コンポーネント。UVスクロール・幅の脈動・ビーム長を毎フレーム更新する。 | 3/3 |
| [`rotatingPlatform`](reference/Devices/rotatingPlatform.md) | 指定軸・角度・速度で回転を繰り返す足場。1回転後に`rotationDelay`だけ待って再び回り始める。 | 3/3 |
| [`vendingMachine`](reference/Devices/vendingMachine.md) | 自販機型のオブジェクト生成器。有効時のみ、指定位置（半径内のランダム位置も可）にプレハブを出現させる。 | 3/3 |
| [`elevatorFloorsPanel`](reference/Devices/elevatorFloorsPanel.md) | エレベーターの階数ボタンを階数分だけ生成し、押された階へ`elevatorSystem`経由で移動させるUIパネル。 | 2/2 |
| [`laserReceiver`](reference/Devices/laserReceiver.md) | 色付きレーザーを受けて接続先オブジェクトの関数を呼ぶレシーバー。接続中は内部の円柱が回転し続ける。 | 2/2 |
| [`rechargerStation`](reference/Devices/rechargerStation.md) | プレイヤーが入ると体力とエネルギーを`healSpeed`で回復する充填ステーション。満タンで停止し、アニメと効果音を制御する。 | 2/2 |
| [`refractionCube`](reference/Devices/refractionCube.md) | レーザーを屈折させるプリズム。設定色を自身へ反映し、屈折中かどうかを外部へ公開する。 | 2/2 |
| [`jumpPlatform`](reference/Devices/jumpPlatform.md) | 触れたプレイヤー・乗り物・任意の剛体を打ち上げるジャンプ台。対象種別や設定に応じ力を加える方法を変える。 | 1/1 |
| [`laserDevice`](reference/Devices/laserDevice.md) | レーザーの発射側。レイキャストでヒットを判定し、シールドやダメージ処理、コネクタへの受け渡しを行う。 | 1/1 |

## ラジオ

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`radioSystem`](reference/Devices/radioSystem.md) | 曲リストと `AudioSource` を管理し、再生・停止・一時停止・次/前/ランダム曲・音量・スライダーと曲名表示を更新する。曲は `songsManager` から取得する。 | 17/17 |
| [`songsManager`](reference/Devices/songsManager.md) | フォルダ内の音声ファイルと内部リストを読み込み、ラジオ用の曲リストを提供するシングルトン管理。 | 3/3 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- 開閉アニメ・カメラ移動・音・UI テキスト・イベント発火・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

