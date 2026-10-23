# otherPowers

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Powers/otherPowers.cs:8`
- **属性**: `System.Serializable`

**概要**: プレイヤーの特殊パワー（念力・発射・重力・時間など）を管理するコンポーネント。パワー選択や照準/フリーファイア、発射物の生成と放物線・追尾、エネルギー消費と回復、HUD・IK・カメラ連携を担う。

**公式ドキュメント抜粋**（[Other Powers](../../docs/player-controller-components/player-controller/other-powers.md)）

> Used to configure the different powers that the player can use to fire energy from his hands and use other type of abilities, which can be extended to add new ones, similar to the weapon system or the ability system itself

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Powers Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Change Powers With Number Keys Active | `changePowersWithNumberKeysActive` | `bool` | true | 数字キー入力でのパワー選択を有効にする。 / 表示条件: `showSettings` がオンのとき |
| Change Powers With Mouse Wheel Active | `changePowersWithMouseWheelActive` | `bool` | true | マウスホイールでのパワー切り替えを有効にする。 / 表示条件: `showSettings` がオンのとき |
| Change Powers With Keys Active | `changePowersWithKeysActive` | `bool` | true | キー割り当てによる前後のパワー切り替えを有効にする。 / 表示条件: `showSettings` がオンのとき |

### Target Detection Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Layer To Damage | `layerToDamage` | `LayerMask` | – | 射撃判定のレイキャストが対象とするレイヤー。 / 表示条件: `showSettings` がオンのとき |

### Energy Stat Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Stats Manager | `playerStatsManager` | `playerStatsSystem` | – | パワー量を同期する`playerStatsSystem`の参照。 / 表示条件: `showSettings` がオンのとき |
| Energy Stat Name | `energyStatName` | `string` | "Current Energy" | パワー量を同期するステータス名の文字列。 / 表示条件: `showSettings` がオンのとき |
| Ignore Check Player States Manager To Fire Projectiles | `ignoreCheckPlayerStatesManagerToFireProjectiles` | `bool` | – | ONにするとステータス値の確認を飛ばして発射する。 / 表示条件: `showSettings` がオンのとき |

### Powers Movements Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Fire Powers Without Aiming | `canFirePowersWithoutAiming` | `bool` | – | ONならエイムせずに射撃ボタンだけで発射できる。 / 表示条件: `showSettings` がオンのとき |
| Use Aim Camera On Free Fire Mode | `useAimCameraOnFreeFireMode` | `bool` | – | 非エイム射撃のときもエイムカメラへ切り替える。 / 表示条件: `showSettings` がオンのとき |
| Time To Stop Aim After Stop Firing | `timeToStopAimAfterStopFiring` | `float` | 0.85f | 射撃停止後、自動でエイムを解除するまでの秒数。 / 表示条件: `showSettings` がオンのとき |
| Use Lower Rotation Speed Aimed Third Person | `useLowerRotationSpeedAimedThirdPerson` | `bool` | – | ONにすると三人称エイム中のカメラ回転速度を下げる。 / 表示条件: `showSettings` がオンのとき |
| Vertical Rotation Speed Aimed In Third Person | `verticalRotationSpeedAimedInThirdPerson` | `float` | 4 | 三人称エイム中の縦方向カメラ回転速度。 / 表示条件: `showSettings.boolValue && useLowerRotationSpeedAimedThirdPerson.boolValue` |
| Horizontal Rotation Speed Aimed In Third Person | `horizontalRotationSpeedAimedInThirdPerson` | `float` | 4 | 三人称エイム中の横方向カメラ回転速度。 / 表示条件: `showSettings.boolValue && useLowerRotationSpeedAimedThirdPerson.boolValue` |
| Run When Aiming Power In Third Person | `runWhenAimingPowerInThirdPerson` | `bool` | – | ONにすると三人称エイム時に走行状態へ切り替える。 / 表示条件: `showSettings` がオンのとき |
| Stop Run If Previously Not Running | `stopRunIfPreviouslyNotRunning` | `bool` | – | エイム前に走っていなければ終了時に走りを止める。 / 表示条件: `showSettings.boolValue && runWhenAimingPowerInThirdPerson.boolValue` |
| Use Upper Body Rotation System To Aim | `useUpperBodyRotationSystemToAim` | `bool` | true | ONにすると上半身IKでエイム方向へ体を向ける。 / 表示条件: `showSettings` がオンのとき |

### Power Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Powers Info Panel | `powersInfoPanel` | `GameObject` | – | パワーモード中だけ表示するUIパネル。 / 表示条件: `showSettings` がオンのとき |

### Power Rotation Point Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Power Rotation Point | `usePowerRotationPoint` | `bool` | – | ONにするとエイム時に専用の回転ポイントを使う。 / 表示条件: `showSettings` がオンのとき |
| Power Rotation Point | `powerRotationPoint` | `Transform` | – | エイム時に上半身IKが基準とするTransform。 / 表示条件: `showSettings.boolValue && usePowerRotationPoint.boolValue` |

### Powers Mode Active Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On State Change | `useEventsOnStateChange` | `bool` | – | ONにするとパワーモード開始と終了でイベントを呼ぶ。 / 表示条件: `showSettings` がオンのとき |
| Even On State Enabled | `evenOnStateEnabled` | `UnityEvent` | – | パワーモード開始時に実行するイベント。 / 表示条件: `showSettings.boolValue && useEventsOnStateChange.boolValue` |
| Event On State Disabled | `eventOnStateDisabled` | `UnityEvent` | – | パワーモード終了時に実行するイベント。 / 表示条件: `showSettings.boolValue && useEventsOnStateChange.boolValue` |
| Use Event On Start Stop Aim | `useEventOnStartStopAim` | `bool` | – | ONにするとエイム開始と解除でイベントを呼ぶ。 / 表示条件: `showSettings` がオンのとき |
| Event On Start Aim | `eventOnStartAim` | `UnityEvent` | – | エイム開始時に実行するイベント。 / 表示条件: `showSettings.boolValue && useEventOnStartStopAim.boolValue` |
| Event On Stop Aim | `eventOnStopAim` | `UnityEvent` | – | エイム解除時に実行するイベント。 / 表示条件: `showSettings.boolValue && useEventOnStartStopAim.boolValue` |

### Player Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Shoot Zone Audio Source | `shootZoneAudioSource` | `AudioSource` | – | 全パワーの発射音を再生するAudioSource。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | 発射方向やレイキャストに使うカメラのTransform。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Main Camera | `mainCamera` | `Camera` | – | シーカー弾の標的探索に使うカメラ。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Upper Body Rotation Manager | `upperBodyRotationManager` | `upperBodyRotationSystem` | – | 上半身の回転IKを制御する`upperBodyRotationSystem`。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| IK System Manager | `IKSystemManager` | `IKSystem` | – | 腕のIKやリコイルを制御する`IKSystem`。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Player Camera Manager | `playerCameraManager` | `playerCamera` | – | カメラ制御を受け持つ`playerCamera`。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Head Bob Manager | `headBobManager` | `headBob` | – | 発射時の画面揺れを担当する`headBob`。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Weapons Manager | `weaponsManager` | `playerWeaponsManager` | – | しゃがみIDの切り替えに使う武器管理の参照。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | 移動や走行を制御する`playerController`。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Grab Objects Manager | `grabObjectsManager` | `grabObjects` | – | エイム時に掴んだ物を落とす`grabObjects`。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Head Track Manager | `headTrackManager` | `headTrack` | – | エイム時の頭部トラッキングを制御する参照。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Impact Decal Manager | `impactDecalManager` | `decalManager` | – | 着弾デカールを管理する`decalManager`。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Player Input | `playerInput` | `playerInputManager` | – | パワー操作の入力を読み取る`playerInputManager`。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Powers Manager | `powersManager` | `powersListManager` | – | パワースロット編集画面の`powersListManager`。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Player Collider | `playerCollider` | `Collider` | – | 自身への射撃判定を除外するコライダー。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Cursor Rect Transform | `cursorRectTransform` | `RectTransform` | – | エイムアシストでカーソル位置を追うRectTransform。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |
| Parable | `parable` | `launchTrayectory` | – | 発射軌道ラインを表示する`launchTrayectory`。 / 表示条件: `showSettings.boolValue && showElements.boolValue` |

### Free Fire Mode Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Free Aim Mode | `useFreeAimMode` | `bool` | – | ONにすると腕の振り向きで狙うフリーエイムを使う。 / 表示条件: `showAimSettings` がオンのとき |
| Free Aim Modee Active | `freeAimModeeActive` | `bool` | – | フリーエイムが現在有効かどうかの状態フラグ。 / 表示条件: `showAimSettings` がオンのとき |
| Arms Pivot Rotation Transform | `armsPivotRotationTransform` | `Transform` | – | フリーエイム時に回転させる腕のピボット。 / 表示条件: `showAimSettings` がオンのとき |
| Arms Pivot Rotation Speed | `armsPivotRotationSpeed` | `float` | 10 | 腕ピボットが目標角度へ追従する速さ。 / 表示条件: `showAimSettings` がオンのとき |
| Arms Pivot Clamp Rotation | `armsPivotClampRotation` | `float` | 60 | 腕ピボットの回転角を制限する上限（度）。 / 表示条件: `showAimSettings` がオンのとき |
| Arms Pivot Rotation Multiplier | `armsPivotRotationMultiplier` | `float` | 1 | 腕ピボットの回転角に掛ける倍率。 / 表示条件: `showAimSettings` がオンのとき |
| Free Aim Mod Look In Opposite Direction Extra Range | `freeAimModLookInOppositeDirectionExtraRange` | `float` | 10 | 逆向きを向いたときに腕の左右を切り替える角度の余裕。 / 表示条件: `showAimSettings` がオンのとき |
| Free Aim Mode Player Status ID | `freeAimModePlayerStatusID` | `int` | -1 | フリーエイム中に切り替えるプレイヤーステータスID。 / 表示条件: `showAimSettings` がオンのとき |

### Other Aim Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Crouch When Using Powers On Third Person | `canCrouchWhenUsingPowersOnThirdPerson` | `bool` | true | OFFにするとしゃがみ中は三人称エイムを開始できない。 / 表示条件: `showAimSettings` がオンのとき |
| Set New Animator Crouch ID | `setNewAnimatorCrouchID` | `bool` | – | ONにするとエイム中にしゃがみIDを差し替える。 / 表示条件: `showAimSettings` がオンのとき |
| New Animator Crouch ID | `newAnimatorCrouchID` | `int` | – | エイム中に使うしゃがみアニメーションのID。 / 表示条件: `showAimSettings` がオンのとき |

### Powers List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| General Attack Damage Multiplier | `generalAttackDamageMultiplier` | `float` | 1 | 全パワーの弾ダメージに掛ける共通倍率。 / 表示条件: `showShootSettings` がオンのとき |
| Initial Power Index | `initialPowerIndex` | `int` | 0 | 開始時に選択されるパワーのリスト番号。 / 表示条件: `showShootSettings` がオンのとき |

### Head Look Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Head Look When Aiming | `headLookWhenAiming` | `bool` | – | ONにするとエイム中に頭部を標的へ向ける。 / 表示条件: `showShootSettings` がオンのとき |
| Head Look Speed | `headLookSpeed` | `float` | – | エイム中の頭部ルックの追従速度。 / 表示条件: `showShootSettings.boolValue && headLookWhenAiming.boolValue` |
| Head Look Target | `headLookTarget` | `Transform` | – | エイム中に頭部が注視するTransform。 / 表示条件: `showShootSettings.boolValue && headLookWhenAiming.boolValue` |

### Aim Assist Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Aim Assist In Third Person | `useAimAssistInThirdPerson` | `bool` | – | ONにすると三人称でカメラのエイムアシストを使う。 / 表示条件: `showShootSettings` がオンのとき |
| Use Max Distance To Camera Center Aim Assist | `useMaxDistanceToCameraCenterAimAssist` | `bool` | – | ONにすると画面中心からの距離上限を適用する。 / 表示条件: `showShootSettings` がオンのとき |
| Max Distance To Camera Center Aim Assist | `maxDistanceToCameraCenterAimAssist` | `float` | – | アシスト対象とする画面中心からの最大距離。 / 表示条件: `showShootSettings.boolValue && useMaxDistanceToCameraCenterAimAssist.boolValue` |
| Use Aim Assist In Locked Camera | `useAimAssistInLockedCamera` | `bool` | true | ONなら固定カメラでも注視対象を設定する。 / 表示条件: `showShootSettings` がオンのとき |

### Power Amount Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Projectiles Pool Enabled | `projectilesPoolEnabled` | `bool` | true | ONにすると発射物をプールから再利用する。 / 表示条件: `showShootSettings` がオンのとき |
| Max Amount Of Pool Elements On Weapon | `maxAmountOfPoolElementsOnWeapon` | `int` | 30 | プールに保持する発射物の最大数。 / 表示条件: `showShootSettings` がオンのとき |
| Infinite Power | `infinitePower` | `bool` | – | ONにするとパワーを消費しなくなる。 / 表示条件: `showShootSettings` がオンのとき |

### Regenerate Power Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Regenerate Power | `regeneratePower` | `bool` | – | ONにすると時間経過でパワーが回復する。 / 表示条件: `showShootSettings.boolValue && !infinitePower.boolValue` |
| Constant Regenerate | `constantRegenerate` | `bool` | – | ONなら毎秒少しずつ、OFFなら一定量ずつ回復する。 / 表示条件: `!infinitePower.boolValue && regeneratePower.boolValue` |
| Regenerate Time | `regenerateTime` | `float` | – | パワー使用後、回復が始まるまでの待ち時間（秒）。 / 表示条件: `!infinitePower.boolValue && regeneratePower.boolValue` |
| Regenerate Speed | `regenerateSpeed` | `float` | 0 | 1秒あたりに回復するパワー量。 / 表示条件: `regeneratePower.boolValue && constantRegenerate.boolValue` |
| Regenerate Amount | `regenerateAmount` | `float` | – | 回復1回で加算されるパワー量。 / 表示条件: `regeneratePower.boolValue && !constantRegenerate.boolValue` |

### Powers Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Target For Scorch Layer | `targetForScorchLayer` | `LayerMask` | – | 焦げ跡デカールを配置する対象のレイヤー。 / 表示条件: `showShootSettings` がオンのとき |
| Main Decal Manager Name | `mainDecalManagerName` | `string` | "Decal Manager" | デカールマネージャを検索するときの名前。 / 表示条件: `showShootSettings` がオンのとき |

### AI Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Used By AI | `usedByAI` | `bool` | – | ONにするとAIが操作するキャラクターとして扱う。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `choosedPower` | `int` | 0 | – |
| `settings` | `powersSettings` | new powersSettings () | – |
| `aimsettings` | `aimSettings` | new aimSettings () | – |
| `shootsettings` | `shootSettings` | new shootSettings () | – |
| `usingPowers` | `bool` | false | – |
| `auxPowerAmount` | `float` | – | – |
| `showSettings` | `bool` | – | – |
| `showAimSettings` | `bool` | – | – |
| `showShootSettings` | `bool` | – | – |
| `aimingInThirdPerson` | `bool` | – | – |
| `aimingInFirstPerson` | `bool` | – | – |
| `shooting` | `bool` | – | – |
| `powersModeActive` | `bool` | – | – |
| `usingFreeFireMode` | `bool` | – | – |
| `checkToKeepPowersAfterAimingPowerFromShooting` | `bool` | – | – |
| `aimModeInputPressed` | `bool` | – | – |
| `weaponAimedFromFiringActive` | `bool` | – | – |
| `rotationPointInfo` | `weaponRotationPointInfo` | – | – |
| `currentPowerName` | `string` | – | – |
| `amountPowersEnabled` | `int` | – | – |
| `actionActive` | `bool` | – | – |
| `firstPersonActive` | `bool` | – | – |
| `canMove` | `bool` | – | – |
| `touching` | `bool` | – | – |
| `showElements` | `bool` | – | – |
| `impactDecalList` | `string []` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setShootZoneParent(Transform newParent, Vector3 newPosition)` | カスタム親が有効ならそれを優先し、`shootZone`の親・位置・回転を設定する。 |
| `setCustomShootZoneParentActiveState(bool state, Transform newParent)` | カスタム親の状態を保存し、有効なら射撃位置をそこへ、無効なら右腕側へ戻す。 |
| `setTouchingMenuPanelState(bool state)` | `fingerPressingTouchPanel`を状態に設定するだけ。 |
| `disableFreeFireModeAfterStopFiring()` | 頭トラッキングと照準維持フラグを戻し、`useAimMode`を呼んで射撃後の構えを解除する。 |
| `resetPowerFiringAndAimingIfPlayerDisabled()` | パワーモード中なら射撃・照準・フリーファイア・IKをまとめて解除して待機状態に戻す。 |
| `playerIsBusy()` | デバイス使用中かサブメニュー・メニュー表示中ならtrueを返す（ターン制ならfalse）。 |
| `useAimMode()` | 移動可能な三人称で、しゃがみ解除や`aimOrKeepPower`を経て照準の有効/無効と走りを切り替える。 |
| `aimOrKeepPower()` | 一人称/三人称の照準状態を反転し、必要ならしゃがみアニメIDを設定する。 |
| `aimOrKeepPowerInThirdPerson(bool state)` | 三人称の照準フラグと`setAimingPowersState`を設定し、解除時は射撃照準フラグも消す。 |
| `aimOrKeepPowerInFirstPerson(bool state)` | 一人称の照準フラグを設定し、プレイヤーに照準状態を通知する。 |
| `isAimingPower()` | 一人称または三人称で照準中かを返す。 |
| `isAimingPowerInFirstPerson()` | 一人称の照準フラグを返すだけ。 |
| `isAimingPowerInThirdPerson()` | 三人称の照準フラグを返すだけ。 |
| `keepPower()` | 一人称・三人称の照準を両方falseにして構えを解除する。 |
| `setAimOrKeepPowerState(bool firstPersonState, bool thirdPersonState)` | 一人称・三人称の照準状態を引数の値にまとめて設定する。 |
| `updateProjectileInfoValuesOnAllPowers()` | 0.3秒間隔で全パワーの発射物情報を作り直し、現在のパワーを復元する。 |
| `enableMuzzleFlashLight()` | マズルフラッシュ使用時のみ、既存コルーチンを止めて指定時間だけライトを点灯させる。 |
| `usePowerBar(float amount)` | 無限でなければ残量を`amount`だけ減らし、補助値と最終使用時刻を更新してスライダーへ反映する。 |
| `isThereEnergy()` | 残量が0より大きいか無限ならtrueを返す。 |
| `updateSlider(float value)` | パワーバーとテキストを更新し、統計マネージャーにもエネルギー値を通知する。 |
| `getEnergy(float amount)` | 生存中なら残量を加算して最大値でクランプし、スライダー更新と補助値反映を行う。 |
| `removeEnergy(float amount)` | 残量を`amount`だけ減らして0未満をクランプし、スライダーと補助値を更新する。 |
| `getCurrentEnergyAmount()` | 現在のエネルギー量を返す。 |
| `getMaxEnergyAmount()` | 最大エネルギー量を返す。 |
| `getAuxEnergyAmount()` | 補助エネルギー量`auxPowerAmount`を返す。 |
| `addAuxEnergyAmount(float amount)` | 補助エネルギー量に`amount`を加算するだけ。 |
| `getEnergyAmountToLimit()` | 上限までの残り量（最大値−補助値）を返す。 |
| `increaseMaxPowerAmount(float newAmount)` | 最大エネルギー量を加算し、スライダーの最大値も更新する。 |
| `setPowerAmountOnMaxValue()` | 差分を`getEnergy`で加算して残量を最大値にする。 |
| `updateSliderMaxValue(float newMaxValue)` | パワーバーがあれば最大値だけを設定する。 |
| `initializePowerAmount(float newValue)` | エネルギー量を指定値に初期化するだけ。 |
| `initializeMaxPowerAmount(float newValue)` | 最大エネルギー量を指定値に初期化するだけ。 |
| `initializeRegenerateSpeed(float newValue)` | 回復速度を指定値に設定するだけ。 |
| `increaseRegenerateSpeed(float newValue)` | 回復速度に`newValue`を加算するだけ。 |
| `updateEnergyAmountWithoutUpdatingStatManager(int statId, float amount)` | 統計マネージャーを介さず残量を設定し、内部スライダーと補助値だけ更新する。 |
| `updateMaxEnergyAmountWithoutUpdatingStatManager(int statId, float amount)` | 統計を介さず最大量を設定し、スライダーの最大値も更新する。 |
| `updateRegenerateSpeedAmountWithoutUpdatingStatManager(int statId, float amount)` | 統計を介さず回復速度を設定するだけ。 |
| `setGeneralAttackDamageMultiplierValue(float newValue)` | 攻撃ダメージ倍率を設定するだけ。 |
| `generalAttackDamageMultiplierIncreaseStat(float extraValue)` | ダメージ倍率を加算し、全パワーの発射物情報を更新する。 |
| `initializeGeneralAttackDamageMultiplierStatAmount(float newValue)` | ダメージ倍率を指定値に初期化するだけ。 |
| `getGeneralAttackDamageMultiplierValue()` | ダメージ倍率の現在値を返す。 |
| `chooseNextPower()` | 有効パワーが複数なら次の番号キーのパワーを探して選択し、表示を更新する。 |
| `choosePreviousPower()` | 前の番号キーの有効パワーを逆順に探して選択し、表示を更新する。 |
| `checkParableTrayectory(bool parableState)` | 現在のパワーと視点設定に応じて放物線ラインの表示を切り替える。 |
| `changePowerState(Powers powerToCheck, int numberKey, bool value, int index)` | パワーの番号キーと有効状態を変更し、有効数に応じて選択中パワーやHUDアイコンを更新する。 |
| `setPower(Powers power)` | 名前が一致する有効パワーを選択し、HUDのテクスチャを切り替える。 |
| `resetLastAmountOfFiredProjectiles()` | 発射数カウンタを0に戻すだけ。 |
| `getLastAmountOfFiredProjectiles()` | 直近の発射数を返す。 |
| `shootPower(bool state)` | バースト中でなければ残量>0のときだけ射撃を開始し、`powerShoot`と最終発射時刻更新を行う。 |
| `powerShoot(bool shootAtKeyDown)` | 連射間隔と残量・掴み状態を確認し、音・消費・発射物生成（放物線/シーカー/レイ）や反動を実行する。 |
| `canPlayerMove()` | `canMove`を返す。 |
| `isActionActiveInPlayer()` | プレイヤーのアクション実行状態を返す。 |
| `checkPowerAbility(bool keyDown)` | 能力持ちパワーなら、押下時はdown、離した時はupのイベントを呼ぶ。 |
| `activateSecondaryAction()` | サブアクション使用時に対応するイベントを実行する。 |
| `launchCurrentProjectile(Rigidbody projectileRigdibody, Vector3 cameraDirection)` | Kinematicを解除し、放物線速度か前方へのインパルスで発射物を飛ばす。 |
| `setProjectileSpread()` | `spreadAmount`の範囲でXYZのランダムな拡散角を返す。 |
| `checkAutoShootOnTag()` | タグ自動射撃が有効ならカメラからレイを飛ばし、対象タグ検出で自動射撃を開始、外れたらリセットする。 |
| `setSeekerProjectileInfo()` | カメラを取得し、索敵位置・タグ・画面条件を渡して最近接の敵を返す。 |
| `createShootParticles()` | 射撃パーティクルがあればプールまたは生成で射撃位置に出現させる。 |
| `setLastTimeFired()` | 最終発射時刻を記録し、プレイヤー側にも通知する。 |
| `getLastTimeFired()` | 最終発射時刻を返す。 |
| `death(bool state)` | 死亡フラグを設定し、死亡時は一人称でなければ照準を解除する。 |
| `activateAimMode()` | 掴み物体の解除、カメラ照準、IK・上半身回転・照準支援・放物線・イベントをまとめて有効化する。 |
| `deactivateAimMode()` | 照準に伴うカメラ・IK・ヘッドトラック・照準支援・カーソル・イベントを解除し、掴み物体を落とす。 |
| `enableOrDisableIKOnPowersDuringAction(bool state)` | `actionActive`を反転設定し、上半身IK・ヘッドトラック・腕状態を切り替える。 |
| `setActionActiveState(bool state)` | `actionActive`を設定するだけ。 |
| `fireHomingProjectiles()` | 索敵済みの各敵へ発射物を生成して追尾させ、音・消費・反動を実行してアイコンを消す。 |
| `activatePowerHandRecoil()` | 反動設定があるパワーならIKシステムに反動を開始させる。 |
| `enableOrDisablePowerCursor(bool state)` | カーソルを表示/非表示し、表示時はカスタムレティクルを更新、非表示時は位置を戻す。 |
| `checkCustomReticle()` | 現在のパワーの設定に応じてカスタム/通常レティクルを切り替え、画像を差し替える。 |
| `changePlayerMode(bool state)` | パワーカーソルと放物線表示を状態に合わせて切り替える。 |
| `changeCameraToThirdOrFirstView(bool isFirstPersonActive)` | 照準を解除して射撃位置をカメラ/手に付け替え、照準状態とカーソル・使用中フラグを更新する。 |
| `setAimModeSide(bool state)` | 右/左腕を切り替えて`handActive`と`usingRightArm`を更新し、三人称なら射撃位置も移す。 |
| `isUsingPowers()` | `usingPowers`を返す。 |
| `setUsingPowersState(bool state)` | 使用中フラグを設定し、プレイヤー側にも通知する。 |
| `checkPowerShake()` | 揺れ設定があるパワーなら、一人称/三人称に応じた射撃シェイクを頭部に設定する。 |
| `setPowersModeState(bool state)` | パワーモード状態を設定し、解除時はフリーファイアを停止、イベントと情報パネルを更新する。 |
| `enableOrDisablePowersInfoPanel(bool state)` | パネルがあれば表示状態を切り替える。 |
| `checkEventsOnStateChange(bool state)` | イベント使用時、有効/無効に応じたUnityEventを発火する。 |
| `checkEventsOnAimStateChange(bool state)` | 照準イベント使用時、開始/終了のUnityEventを発火する。 |
| `checkIfChangePlayerMode()` | パワー使用中なら`changePlayerMode(true)`を呼ぶ。 |
| `checkIfChangePlayerModeAccordingToViewType()` | 一人称かどうかに応じて`changePlayerMode`を呼び分ける。 |
| `isPowersModeActive()` | パワーモードが有効かを返す。 |
| `isFirstPersonActive()` | 一人称かどうかを返す。 |
| `disableFreeFireModeState()` | 射撃由来の照準・フリーファイア関連フラグとカメラ状態をまとめて解除する。 |
| `setOtherPowersInputPausedState(bool state)` | 入力停止フラグを設定し、停止時は射撃中なら射撃を止める。 |
| `setBurstModeState(bool state)` | 現在のパワーのバースト設定を変更するだけ。 |
| `setBurstAmount(int newAmount)` | 現在のパワーのバースト数を設定するだけ。 |
| `isShootingBurst()` | バースト射撃中かを返す。 |
| `inputNextOrPreviousPowerByButton(bool setNextPower)` | キー切替が有効で入力可能なとき、次/前のパワー選択を実行する。 |
| `inputNextOrPreviousPowerByMouse(bool setNextPower)` | マウスホイール切替時、掴み中でズーム使用中を除いて次/前のパワーを選ぶ。 |
| `inputHoldOrReleaseShootPower(bool holdingButton)` | 射撃ボタンの押下/解放に応じ、フリーファイア照準や自動/バースト射撃、解放時のホーミング発射を制御する。 |
| `inputHoldShootPower()` | 射撃ボタン保持時、フリーファイア照準を整え、自動かつ非バーストのパワーを射撃する。 |
| `inputSetAimPowerState(bool state)` | 照準入力フラグを設定して`useAimMode`を呼ぶ。 |
| `inputAimPower()` | 照準入力フラグを反転して`useAimMode`を呼ぶ。 |
| `inputActivateSecondaryAction()` | 入力可能かつパワーモード中なら`activateSecondaryAction`を呼ぶ。 |
| `setRunEnabledState(bool state)` | 走り（スプリント）の有効状態をプレイヤーに設定するだけ。 |
| `setShootEnabledState(bool state)` | `settings.shootEnabled`を設定するだけ。 |
| `setCurrentPowerByName(string powerName)` | 名前一致の有効パワーを選択し、HUDを更新して選択アイコンを消す。 |
| `shootPowerExternally()` | 三人称照準を一時的に立てて射撃を開始・停止し、照準を戻す。 |
| `shootPowerExternally(string powerName)` | 指定パワーに切り替えてから外部射撃を実行する。 |
| `shootPowerExternallyAndResetLastShoot(string powerName)` | 指定パワーで外部射撃し、連射間隔のタイマーをリセットする。 |
| `resetLastShoot()` | `lastShoot`を0に戻すだけ。 |
| `enableRegularPowerListElement(string powerName)` | 該当パワーを有効化し、スロット・有効数・選択・HUDを更新する。 |
| `disableRegularPowerListElement(string powerName)` | 該当パワーを無効化し、スロットと有効数を更新する。 |
| `updateAmountPowersEnabled()` | 有効なパワー数をスロット上限まで数え直す。 |
| `getNumberOfPowersAvailable()` | 有効なパワーの総数を数えて返す。 |
| `setFirstPowerAvailable()` | 最初の有効パワーを選択し、無ければHUDアイコンを消す。 |
| `setSelectedPowerIconState(bool state)` | 選択パワーアイコンの表示状態を切り替える。 |
| `getCurrentPower()` | 現在選択中のパワーを返す。 |
| `getPowerIndexByNumberKey(int numberKeyToSearch)` | 番号キーが一致する有効パワーのインデックスを返し、無ければ-1を返す。 |
| `enableOrDisableAllPowers(bool state)` | 全パワーの有効状態を一括設定し、コンポーネントを更新する。 |
| `setUsedByAIState(bool state)` | AI使用フラグを設定するだけ。 |
| `updateComponent()` | `GKC_Utils.updateComponent`でこのコンポーネントを更新する。 |
| `getImpactListInfo()` | デカールマネージャーを取得してインパクト名一覧を配列に詰め、コンポーネントを更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `evenOnStateEnabled` | `UnityEvent` | – |
| `eventOnStateDisabled` | `UnityEvent` | – |
| `eventOnStartAim` | `UnityEvent` | – |
| `eventOnStopAim` | `UnityEvent` | – |

## 内部型

- `powersSettings`（class）
- `aimSettings`（class）
- `shootSettings`（class）
- `Powers`（class）
- `powerInfo`（class）
