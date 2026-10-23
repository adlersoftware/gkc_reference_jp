# Others メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Others/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **89 型 / 470 メソッド**
- 注釈付き: **470 メソッド**（100%）
- 生成元: 各 `.cs` の実装。共通ユーティリティ、スポナー、スキャナー、UI 補助など雑多なコンポーネント群。

## Console Mode

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`consoleMode`](reference/Others/consoleMode.md) | ゲーム内デバッグコンソールで、キー入力からコマンド文字列を組み立て、登録済みコマンドの検証・実行、補完、履歴、オブジェクトのスポーンを行う。 | 22/22 |

## Scanner System

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`scannerSystem`](reference/Others/scannerSystem.md) | 一人称視点のスキャナーモードを制御するコンポーネントで、注視対象のスキャン進捗スライダー、カメラFOV/ズーム、弱点表示、入力イベントをまとめて扱う。 | 24/24 |
| [`simpleScannerSystem`](reference/Others/simpleScannerSystem.md) | スキャナーカメラの有効状態を切り替え、`cullingMask`とイベントを更新する。 | 2/2 |

## （直下）

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`BezierSpline`](reference/Others/BezierSpline.md) | 3次ベジェスプラインを制御点・モード・ループ設定で管理するコンポーネントで、位置/速度/方向の取得や最近点探索、エディタでのカーブ追加削除を提供する。 | 21/21 |
| [`spawnObject`](reference/Others/spawnObject.md) | プレハブやオブジェクトを指定位置に生成するコンポーネントで、生成数・上限・プール利用・リモートイベント送信などを設定できる。 | 19/19 |
| [`hideBodyPartOnCharacterSystem`](reference/Others/hideBodyPartOnCharacterSystem.md) | キャラクターのボーンをマウントポイント名で指定して非表示にするコンポーネントで、スケール0化・コライダー切替・バレットタイム併用・非表示リストの復元を扱う。 | 18/18 |
| [`destroyGameObject`](reference/Others/destroyGameObject.md) | オブジェクトを一定時間後や条件成立時に破棄、または非アクティブ化するコンポーネントで、プール返却や付随オブジェクトの同時処理にも対応する。 | 13/13 |
| [`nonEssentialCharacterElementsManager`](reference/Others/nonEssentialCharacterElementsManager.md) | キャラクターの装飾用オブジェクトをリスト管理するエディタ向けコンポーネントで、名前検索・選択・削除・一括の有効化/無効化を提供する。 | 12/12 |
| [`taskCounterSystem`](reference/Others/taskCounterSystem.md) | タスクの達成数を数えるカウンターで、指定タスクの完了/取消、順序制約、完了・取り消しイベント、リセット処理を提供する。 | 12/12 |
| [`playerOptionsEditorSystem`](reference/Others/playerOptionsEditorSystem.md) | オプション画面の各UI（スクロールバー/スライダー/トグル/ドロップダウン）と設定イベントを対応付けて管理するコンポーネントで、既定値への復元も行う。 | 11/11 |
| [`tagLayerSystem`](reference/Others/tagLayerSystem.md) | Unityエディタ専用（`#if UNITY_EDITOR`）で、ProjectSettings/TagManagerのタグとレイヤーを追加・削除し、一覧を再取得する補助コンポーネント。 | 11/11 |
| [`railMechanism`](reference/Others/railMechanism.md) | レール上のオブジェクトを最終位置や停止位置へ補間移動させ、接続イベントやレール使用状態を管理するコンポーネント。 | 10/10 |
| [`rotateObjectWithRegularUpdate`](reference/Others/rotateObjectWithRegularUpdate.md) | `Update`で毎フレーム`mainTransform`を`speed`と`direccion`に従って回転させ、停止や回転リセットも提供するコンポーネント。 | 10/10 |
| [`rotateObjects`](reference/Others/rotateObjects.md) | `FixedUpdate`で`mainTransform`を`speed`と`direccion`に従って回転させ、停止や回転リセットも提供する物理更新版コンポーネント。 | 10/10 |
| [`simpleSpawnObjectManager`](reference/Others/simpleSpawnObjectManager.md) | カテゴリ別のスポーン情報リストを持ち、名前指定でオブジェクトを出現させたり、有効状態やリモートイベントを切り替える管理コンポーネント。 | 10/10 |
| [`GKCUIManager`](reference/Others/GKCUIManager.md) | 名前付きUI要素のリストをまとめて、または個別に有効/無効化し、名前検索やエディタ上での選択も行うUI管理コンポーネント。 | 10/10 |
| [`spiderControllerInterface`](reference/Others/spiderControllerInterface.md) | クモ型コントローラ（spider controller）とカメラ制御のやり取りを定義する、中身が空の`virtual`メソッドのみの基底クラス。 | 10/10 |
| [`FloatingObject`](reference/Others/FloatingObject.md) | 水面（`waterSurfaceSystem`）上でRigidbodyにボクセル単位の浮力を加え、水中の抵抗や外部力を処理する浮遊オブジェクト。 | 8/8 |
| [`checkCollisionType`](reference/Others/checkCollisionType.md) | 衝突・トリガーの開始/終了/滞在を設定フラグで振り分け、UnityEventやSendMessageで外部へ通知する検出コンポーネント。 | 8/8 |
| [`ignoreCollisionHelper`](reference/Others/ignoreCollisionHelper.md) | 指定レイヤーやタグのオブジェクトとの衝突を`Physics.IgnoreCollision`で無視し、その記録と復帰・一時的な有効化を扱う補助コンポーネント。 | 8/8 |
| [`dissolveObject`](reference/Others/dissolveObject.md) | 対象オブジェクトのマテリアルを溶かしシェーダーで徐々に消し、時間経過後に破棄するまでの演出を管理するコンポーネント。 | 8/8 |
| [`placeObjectInCameraEditorPositionSystem`](reference/Others/placeObjectInCameraEditorPositionSystem.md) | エディタカメラからのレイキャストでオブジェクトを面上に配置し、回転・整列・接地スナップを操作する編集用コンポーネント。 | 8/8 |
| [`simpleAnimationSystem`](reference/Others/simpleAnimationSystem.md) | レガシー`Animation`の指定クリップを前後どちらかへ再生し、開始・終了イベントを発火する簡易アニメーション制御コンポーネント。 | 7/7 |
| [`followObjectPositionSystem`](reference/Others/followObjectPositionSystem.md) | `FixedUpdate`で`objectToFollow`の位置と回転を自身（または`mainTransform`）へ同期する追従コンポーネント。 | 7/7 |
| [`simpleEventSystem`](reference/Others/simpleEventSystem.md) | 有効/無効の2種類（または通常1種類）のUnityEventを持ち、遅延付きの発火と状態保持を行う汎用イベントコンポーネント。 | 7/7 |
| [`objectOnWater`](reference/Others/objectOnWater.md) | `FloatingObject`が継承する水面オブジェクト用の基底クラスで、中身が空の`virtual`メソッドのみを定義する。 | 7/7 |
| [`setRigidbodyStateSystem`](reference/Others/setRigidbodyStateSystem.md) | リストまたは半径検索で集めたRigidbodyをまとめて非キネマティックにし、指定方向の力や爆発力、リモートイベントを適用するコンポーネント。 | 7/7 |
| [`showMessageOnHUDSystem`](reference/Others/showMessageOnHUDSystem.md) | HUD上のメッセージパネルを名前やインデックスで表示・非表示し、表示時間や入力アクション名の置換、ローカライズも扱うコンポーネント。 | 6/6 |
| [`addForceToObjectSystem`](reference/Others/addForceToObjectSystem.md) | 登録したRigidbodyへ毎フレーム風の力を加え、プレイヤー・乗り物・通常オブジェクトで強さを変えつつ風の状態も同期するコンポーネント。 | 6/6 |
| [`waterSurfaceSystem`](reference/Others/waterSurfaceSystem.md) | 水面の高さ・法線・密度などを外部へ提供する基底クラス。各メソッドは`virtual`で既定値だけを返し、実処理は派生クラスが上書きする。 | 6/6 |
| [`windOnObjectState`](reference/Others/windOnObjectState.md) | オブジェクトが風を受けている状態と、その風向き・風力を保持する小さな状態クラス。 | 6/6 |
| [`updateRigidbodyStateInsideRigidbodySystem`](reference/Others/updateRigidbodyStateInsideRigidbodySystem.md) | トリガー内に入ったRigidbodyを親Transformへ親子付けし、プレイヤーならカメラや移動状態も切り替える。 | 5/5 |
| [`enableOrDisableObjectsOnDistanceSystem`](reference/Others/enableOrDisableObjectsOnDistanceSystem.md) | カメラからの距離と画面内判定に応じて、登録オブジェクトの有効状態をまとめて切り替える管理コンポーネント。 | 5/5 |
| [`shakeCharacterBodyPartSystem`](reference/Others/shakeCharacterBodyPartSystem.md) | 人型ボーンの1つを一定時間揺らす演出を行い、対象ボーンを名前かTransformで指定できる。 | 5/5 |
| [`followObjectPositionUpdateSystem`](reference/Others/followObjectPositionUpdateSystem.md) | 指定した`objectToFollow`へ毎フレーム位置と回転を追従させる単純な追従コンポーネント。 | 5/5 |
| [`setCharacterAsChildSystem`](reference/Others/setCharacterAsChildSystem.md) | プレイヤーと子キャラクターを親子関係にし、入力・速度・IK・コライダー衝突を同期させる。 | 5/5 |
| [`setObjectParentSystem`](reference/Others/setObjectParentSystem.md) | 子オブジェクトのリストを指定した親Transformへ付け替える（開始時の自動実行にも対応）。 | 5/5 |
| [`GKCTeleportHelper`](reference/Others/GKCTeleportHelper.md) | シーン上のメインプレイヤーを対象に、テレポート・ダイアログ起動・移動速度の制限をまとめて行う補助コンポーネント。 | 5/5 |
| [`coinPocketSystem`](reference/Others/coinPocketSystem.md) | キャラクターが所持するコイン枚数を管理し、取得時と全ドロップ時にイベントを発火する。 | 5/5 |
| [`flyingTurretSystem`](reference/Others/flyingTurretSystem.md) | 追従対象の周囲に飛行タレットを生成し、手動射撃の有効化やAI制御の切り替えを行う。 | 5/5 |
| [`graphicQualitySettingsSystem`](reference/Others/graphicQualitySettingsSystem.md) | 画質レベル・解像度・ウィンドウ表示・アンチエイリアスを、設定リストの名前指定で切り替える。 | 5/5 |
| [`pauseAnimationSystem`](reference/Others/pauseAnimationSystem.md) | 人型ボーンのTransformをスナップショットで固定し、アニメーションを止めたように見せる。 | 4/4 |
| [`enableOrDisableObjectOnDistanceManager`](reference/Others/enableOrDisableObjectOnDistanceManager.md) | 距離管理システムへ自身を登録する側のコンポーネントで、有効・無効の切り替え時にイベントを発火する。 | 4/4 |
| [`scanElementInfo`](reference/Others/scanElementInfo.md) | スキャン対象の情報を`dataBase.txt`へ保存・削除し、既読状態を管理する。 | 4/4 |
| [`eventObjectFoundOnRaycastSystem`](reference/Others/eventObjectFoundOnRaycastSystem.md) | 指定Transformからレイキャストし、検出オブジェクトが変わった時にイベントやリモートイベントを呼ぶ。 | 4/4 |
| [`moveObjectLateUpdate`](reference/Others/moveObjectLateUpdate.md) | `LateUpdate`でコサイン波に沿ってオブジェクトを往復移動させる簡易コンポーネント。 | 4/4 |
| [`vehiclePassengerUnderwater`](reference/Others/vehiclePassengerUnderwater.md) | 車両の乗員が水中に入ったかをカメラ位置で判定し、水中エフェクト用のイベントを発火する。 | 4/4 |
| [`selectObjectManager`](reference/Others/selectObjectManager.md) | エディタ用のオブジェクト選択支援で、名前検索した結果から階層上の対象を選択する。 | 4/4 |
| [`combineMeshSystem`](reference/Others/combineMeshSystem.md) | 子階層の`MeshFilter`を集めて1つのメッシュに結合し、必要なら`MeshCollider`も付ける。 | 3/3 |
| [`regularVehicleOnWater`](reference/Others/regularVehicleOnWater.md) | 水上を走る車両向けに、乗員の水中判定や浮力、水面の上下で発火するイベントを扱う。 | 3/3 |
| [`checkIfCharacterUsingWeaponsToChangeMode`](reference/Others/checkIfCharacterUsingWeaponsToChangeMode.md) | プレイヤーが武器を使用しているかをコルーチンで監視し、状態変化に応じてモード切替のイベントを扱う。 | 3/3 |
| [`mechanismPart`](reference/Others/mechanismPart.md) | 歯車機構の回転パーツで、速度・回転の有効状態・歯車の装着状態を保持して`Update`で回す。 | 3/3 |
| [`setGameObjectActiveState`](reference/Others/setGameObjectActiveState.md) | 対象`GameObject`のSetActive状態を保持し、反転や開始時の初期化を行う。 | 3/3 |
| [`rotateObjectSmoothlySystem`](reference/Others/rotateObjectSmoothlySystem.md) | 複数の回転状態を名前で切り替え、コルーチンで滑らかに回転させる。 | 3/3 |
| [`simpleLamp`](reference/Others/simpleLamp.md) | ランプの設置状態と点灯を管理し、切り替え時にスイッチ音を鳴らす。 | 3/3 |
| [`showGameInfoHud`](reference/Others/showGameInfoHud.md) | HUD要素を親名と要素名で検索して返し、必要ならパネルをプレハブから生成する。 | 3/3 |
| [`simpleLightingModifier`](reference/Others/simpleLightingModifier.md) | 環境光（アンビエント）の色を一括で変更するだけの小さな設定コンポーネント。 | 3/3 |
| [`setCharacterParentOnMovingObject`](reference/Others/setCharacterParentOnMovingObject.md) | 動くオブジェクトに乗ったプレイヤーや車両を親子付けし、移動プラットフォームとして扱う。 | 2/2 |
| [`simpleBulletTimeOnCharacterEffect`](reference/Others/simpleBulletTimeOnCharacterEffect.md) | キャラクターの移動速度とタイムスケールを下げるスローモーション演出と、メッシュの残像生成を行う。 | 2/2 |
| [`simpleSoundSystem`](reference/Others/simpleSoundSystem.md) | カテゴリ別の効果音リストからランダムに1つ選んで再生する。 | 2/2 |
| [`moveObjectSmoothlySystem`](reference/Others/moveObjectSmoothlySystem.md) | 登録した位置状態へコルーチンでオブジェクトを滑らかに移動させる。 | 2/2 |
| [`setObjectScaleSystem`](reference/Others/setObjectScaleSystem.md) | 名前付きのスケール状態へコルーチンで補間しながら拡大縮小する。 | 2/2 |
| [`UIMouseHoverEvent`](reference/Others/UIMouseHoverEvent.md) | UIへのポインタ進入・退出を検知してUnityEventを呼ぶだけのコンポーネント。 | 2/2 |
| [`enableOrDisableAIOnDistanceManager`](reference/Others/enableOrDisableAIOnDistanceManager.md) | 距離管理からAIキャラクターの有効/無効を切り替え、メッシュ・Animator・カメラも連動させる。 | 2/2 |
| [`headExplodeExample`](reference/Others/headExplodeExample.md) | 頭部パーツを消すデモ用スクリプトで、任意でタイムバレット演出も併用する。 | 2/2 |
| [`replaceMaterialSystem`](reference/Others/replaceMaterialSystem.md) | 対象オブジェクトのマテリアルを一括で差し替え、元のマテリアルへ戻せるようにする。 | 2/2 |
| [`initialPopUpWindow`](reference/Others/initialPopUpWindow.md) | エディタでGKCの初期情報ウィンドウを表示する`EditorWindow`で、`OnGUI`で内容を描画する。 | 1/1 |
| [`playSoundOnTriggerEnter`](reference/Others/playSoundOnTriggerEnter.md) | トリガー進入時に一度だけ効果音を再生する。 | 1/1 |
| [`putGear`](reference/Others/putGear.md) | 歯車がレール上に落ちたかを判定し、持ち主から離して所定位置へはめる。 | 1/1 |
| [`setInitialPositionAtGameStart`](reference/Others/setInitialPositionAtGameStart.md) | ゲーム開始時に登録オブジェクトを指定位置・回転へ移動させる。 | 1/1 |
| [`consoleLogOnScreenSystem`](reference/Others/consoleLogOnScreenSystem.md) | アプリケーションログを`Text`へ蓄積表示し、長すぎる場合は切り詰める。 | 1/1 |
| [`playSoundOnCollision`](reference/Others/playSoundOnCollision.md) | 衝突時に効果音を再生し、最低速度を条件にできる。 | 1/1 |
| [`preventCharacterCollisionOnTop`](reference/Others/preventCharacterCollisionOnTop.md) | キャラクターの上に乗られた時に押し出す力を加え、位置ずれを防ぐ。 | 1/1 |
| [`changeObjectColors`](reference/Others/changeObjectColors.md) | マテリアル群の色を元の色へ時間をかけて戻す補間処理を持つ。 | 1/1 |
| [`ignoreCollisionSystem`](reference/Others/ignoreCollisionSystem.md) | 指定コライダーとの衝突を無視させる設定をまとめて行う。 | 1/1 |
| [`openInitialPopUpWindow`](reference/Others/openInitialPopUpWindow.md) | プレイ開始時に案内用ポップアップウィンドウを開くかどうかを制御するエディタ補助。 | 1/1 |
| [`simpleMoveObjectSystem`](reference/Others/simpleMoveObjectSystem.md) | 対象オブジェクトを目標Transformの位置・回転へ速度に応じて補間移動する。 | 1/1 |
| [`fadeObject`](reference/Others/fadeObject.md) | レンダラーのアルファを下げてオブジェクトを消す演出を行い、プール返却にも対応する。 | 1/1 |
| [`simpleGUILayoutStateManager`](reference/Others/simpleGUILayoutStateManager.md) | シーン内の全`MonoBehaviour`の`useGUILayout`を一括で切り替える。 | 1/1 |
| [`simpleLensFlareSystem`](reference/Others/simpleLensFlareSystem.md) | レンズフレア用オブジェクトを一定時間だけ表示する。 | 1/1 |
| [`FloatingObjectSocket`](reference/Others/FloatingObjectSocket.md) | ソケットに置かれた`FloatingObject`を保持して返すだけの小さなコンポーネント。 | 1/1 |
| [`createMeshDuplicate`](reference/Others/createMeshDuplicate.md) | `SkinnedMeshRenderer`をベイクして静的メッシュの複製を作り、基準オブジェクトの子としてまとめる。 | 1/1 |
| [`filesChecker`](reference/Others/filesChecker.md) | エディタ用のプリファブ検査ツールで、指定パス以下のプレファブの位置・回転・スケールやAudioSourceを確認する。 | 1/1 |
| [`rotatoryGear`](reference/Others/rotatoryGear.md) | 歯車の回転可否フラグを保持するだけの小さなコンポーネント。 | 1/1 |
| [`simpleActionButton`](reference/Others/simpleActionButton.md) | ボタンから指定オブジェクトへ名前でメソッドを送るだけのコンポーネント。 | 1/1 |
| [`simpleCoinPickup`](reference/Others/simpleCoinPickup.md) | コイン取得時にキャラクターの`coinPocketSystem`へ枚数を加算して自身を消す。 | 1/1 |
| [`simpleRandomTextManager`](reference/Others/simpleRandomTextManager.md) | 登録したテキストからランダムまたはID指定で1つ選び、`Text`に表示する。 | 1/1 |
| [`simpleRaycastPlacementDetector`](reference/Others/simpleRaycastPlacementDetector.md) | レイキャストの当たった面に合わせてオブジェクトを配置する。 | 1/1 |
| [`simpleSetQuaternionRotation`](reference/Others/simpleSetQuaternionRotation.md) | 回転を初期化するだけの最小コンポーネント。 | 1/1 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- 状態遷移・イベント発火・UI 更新・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

