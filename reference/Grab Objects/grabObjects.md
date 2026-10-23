# grabObjects

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Grab Objects/grabObjects.cs:7`

**概要**: `grabObjects`は、プレイヤーが注視した剛体オブジェクトを掴んで保持・運搬・投擲・ドロップさせるプレイヤー側コンポーネント。タグとレイヤの一時退避、重量と筋力の判定、IKやカーソル、透明化、`grabPhysicalObjectSystem`による両手持ちまで制御する。

**公式ドキュメント抜粋**（[Grab Objects](../../docs/player-controller-components/player-controller/grab-objects.md)）

> System used to grab objects in a similar way to dead space, with a type of telekinesis, and to grab and carry objects physically on player’s hands, using IK for that as well, and managing the collisions and forces of that object, including to drop or throw it.

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Grab Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Grab Objects Enabled | `grabObjectsEnabled` | `bool` | – | グラブ機能全体の有効/無効。オフだとオブジェクトを掴めない。 |
| Hold Distance | `holdDistance` | `float` | 3 | 掴んだオブジェクトをカメラから離して保持する距離。 |
| Max Distance Held | `maxDistanceHeld` | `float` | 4 | 保持中のオブジェクトがカメラから離れられる最大距離。超えると落とす。 |
| Max Distance Grab | `maxDistanceGrab` | `float` | 10 | オブジェクトを掴める最大距離。検出レイキャストの長さ。 |
| Hold Speed | `holdSpeed` | `float` | 10 | 保持位置へ移動させる速度。`linearVelocity`の係数。 |
| Closest Hold Distance In Fixed Position | `closestHoldDistanceInFixedPosition` | `float` | – | 固定位置グラブ時に手前へ寄せられる最小距離。 |
| Grab In Fixed Position | `grabInFixedPosition` | `bool` | – | 掴んだ瞬間の距離を保ったままカメラに固定して保持する。 |
| Use Grabbed Object Offset Third Person | `useGrabbedObjectOffsetThirdPerson` | `bool` | – | 三人称時に保持位置へオフセットを加える。 |
| Grabbed Object Offset Third Person | `grabbedObjectOffsetThirdPerson` | `Vector3` | – | 三人称時の保持位置オフセット（右・上・前）。 / 表示条件: `useGrabbedObjectOffsetThirdPerson` がオンのとき |
| Current Grab Mode | `currentGrabMode` | `grabMode` | – | グラブ方式。`powers`は念力、`realistic`は物理投擲。 |
| Change Gravity Objects Enabled | `changeGravityObjectsEnabled` | `bool` | true | `powers`モードで投げずに重力方向の操作へ切り替える。 / 表示条件: `currentGrabMode.enumValueIndex == 0` |
| Use Force When Object Dropped | `useForceWhenObjectDropped` | `bool` | – | 短く押して離した時に前方へ力を加える。 |
| Use Force When Object Dropped On Third Person | `useForceWhenObjectDroppedOnThirdPerson` | `bool` | – | 三人称でドロップ時に力を加えるかどうか。 / 表示条件: `useForceWhenObjectDropped` がオンのとき |
| Force When Object Dropped On Third Person | `forceWhenObjectDroppedOnThirdPerson` | `float` | – | 三人称でドロップ時に加える力の値。 / 表示条件: `useForceWhenObjectDropped` がオンのとき |
| Use Force When Object Dropped On First Person | `useForceWhenObjectDroppedOnFirstPerson` | `bool` | – | 一人称でドロップ時に力を加えるかどうか。 / 表示条件: `useForceWhenObjectDropped` がオンのとき |
| Force When Object Dropped On First Person | `forceWhenObjectDroppedOnFirstPerson` | `float` | – | 一人称でドロップ時に加える力の値。 / 表示条件: `useForceWhenObjectDropped` がオンのとき |
| Pause Camera Mouse Wheel While Object Grabbed | `pauseCameraMouseWheelWhileObjectGrabbed` | `bool` | – | 保持中はカメラのホイール操作を止める。 |
| Ignore Drop Melee Weapon If Carried | `ignoreDropMeleeWeaponIfCarried` | `bool` | – | 近接武器を持っている間はグラブ入力を受け付けない。 |

### Detection Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Grabbed Object Tag | `grabbedObjectTag` | `string` | – | 保持中に一時的に付け替えるタグ。ドロップで元に戻す。 |
| Grabbed Object Layer | `grabbedObjectLayer` | `string` | – | 保持中に一時的に変更するレイヤー名。 |
| Can Grab Vehicles | `canGrabVehicles` | `bool` | true | 乗り物も掴める対象に含めるかどうか。 |

### Strength Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Infinite Strength | `useInfiniteStrength` | `bool` | true | 筋力を無視し、重さに関係なく掴めるようにする。 / 表示条件: `showAllSettings.boolValue \|\| showStrengthSettings.boolValue` |
| Strength Amount | `strengthAmount` | `float` | – | 現在の筋力値。オブジェクトの重さがこれを超えると掴めない。 / 表示条件: `showAllSettings.boolValue \|\| showStrengthSettings.boolValue && !useInfiniteStrength.boolValue` |
| Show Current Object Weight | `showCurrentObjectWeight` | `bool` | – | 狙ったオブジェクトの重さをUIに表示する。 / 表示条件: `showAllSettings.boolValue \|\| showStrengthSettings.boolValue && !useInfiniteStrength.boolValue` |
| Weight Panel | `weightPanel` | `GameObject` | – | 重さ表示に使うUIパネルのGameObject。 / 表示条件: `showAllSettings.boolValue \|\| showStrengthSettings.boolValue && !useInfiniteStrength.boolValue` |
| Current Object Weight Text | `currentObjectWeightText` | `Text` | – | 重さを「Kg」で表示するテキスト。 / 表示条件: `showAllSettings.boolValue \|\| showStrengthSettings.boolValue && !useInfiniteStrength.boolValue` |
| Regular Weight Text Color | `regularWeightTextColor` | `Color` | – | 筋力で掴める重さのときの文字色。 / 表示条件: `showAllSettings.boolValue \|\| showStrengthSettings.boolValue && !useInfiniteStrength.boolValue` |
| Too Heavy Weight Text Color | `tooHeavyWeightTextColor` | `Color` | – | 筋力不足で掴めない重さのときの文字色。 / 表示条件: `showAllSettings.boolValue \|\| showStrengthSettings.boolValue && !useInfiniteStrength.boolValue` |

### Strength Stat Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Stats Manager | `playerStatsManager` | `playerStatsSystem` | – | 筋力値を同期する`playerStatsSystem`。 / 表示条件: `showAllSettings.boolValue \|\| showStrengthSettings.boolValue` |
| Strength Amount Stat Name | `strengthAmountStatName` | `string` | "Strength" | 筋力として参照するステータス名。 / 表示条件: `showAllSettings.boolValue \|\| showStrengthSettings.boolValue` |

### Grab Physical Objects Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Grab Objects Physically Enabled | `grabObjectsPhysicallyEnabled` | `bool` | true | `grabPhysicalObjectSystem`による手掴みを有効にする。 / 表示条件: `showAllSettings.boolValue \|\| showGrabPhysicalObjectsSettings.boolValue` |

### Hands List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Place To Carry Physical Objects Third Person | `placeToCarryPhysicalObjectsThirdPerson` | `Transform` | – | 三人称で物理オブジェクトを保持する親Transform。 / 表示条件: `showAllSettings.boolValue \|\| showGrabPhysicalObjectsSettings.boolValue && grabObjectsPhysicallyEnabled.boolValue` |
| Place To Carry Physical Objects First Person | `placeToCarryPhysicalObjectsFirstPerson` | `Transform` | – | 一人称で物理オブジェクトを保持する親Transform。 / 表示条件: `showAllSettings.boolValue \|\| showGrabPhysicalObjectsSettings.boolValue && grabObjectsPhysicallyEnabled.boolValue` |
| Position To Keep Object | `positionToKeepObject` | `Transform` | – | `keepGrabbedObjectState`時に固定する親Transform。 / 表示条件: `showAllSettings.boolValue \|\| showGrabPhysicalObjectsSettings.boolValue && grabObjectsPhysicallyEnabled.boolValue` |
| Translate Physical Object Speed | `translatePhysicalObjectSpeed` | `float` | 5 | 保持位置へオブジェクトを移動させる速さ。 / 表示条件: `showAllSettings.boolValue \|\| showGrabPhysicalObjectsSettings.boolValue && grabObjectsPhysicallyEnabled.boolValue` |
| Show Grab Object Icon Enabled | `showGrabObjectIconEnabled` | `bool` | – | 掴めるオブジェクトの上にアイコンを表示する。 / 表示条件: `showAllSettings.boolValue \|\| showGrabPhysicalObjectsSettings.boolValue && grabObjectsPhysicallyEnabled.boolValue` |
| Key Text | `keyText` | `Text` | – | グラブ用のキーを表示するテキスト。 / 表示条件: `grabObjectsPhysicallyEnabled.boolValue && showGrabObjectIconEnabled.boolValue` |
| Grab Object Icon | `grabObjectIcon` | `GameObject` | – | オブジェクト上に出すアイコンのGameObject。 / 表示条件: `grabObjectsPhysicallyEnabled.boolValue && showGrabObjectIconEnabled.boolValue` |
| Icon Rect Transform | `iconRectTransform` | `RectTransform` | – | アイコンを画面座標で配置するRectTransform。 / 表示条件: `grabObjectsPhysicallyEnabled.boolValue && showGrabObjectIconEnabled.boolValue` |
| Get Closest Device To Camera Center | `getClosestDeviceToCameraCenter` | `bool` | – | 画面中心に最も近いオブジェクトを掴む対象にする。 / 表示条件: `showAllSettings.boolValue \|\| showGrabPhysicalObjectsSettings.boolValue && grabObjectsPhysicallyEnabled.boolValue` |
| Use Max Distance To Camera Center | `useMaxDistanceToCameraCenter` | `bool` | – | 画面中心からの距離で対象を絞り込む。 / 表示条件: `grabObjectsPhysicallyEnabled.boolValue && getClosestDeviceToCameraCenter.boolValue` |
| Max Distance To Camera Center | `maxDistanceToCameraCenter` | `float` | – | 画面中心からこのピクセル距離以内の対象だけ選ぶ。 / 表示条件: `grabObjectsPhysicallyEnabled.boolValue && getClosestDeviceToCameraCenter.boolValue` |
| Pickable Shader | `pickableShader` | `Shader` | – | 保持中に透明化するときに使うシェーダー。 / 表示条件: `showAllSettings.boolValue \|\| showGrabPhysicalObjectsSettings.boolValue && grabObjectsPhysicallyEnabled.boolValue` |
| Default Shader Name | `defaultShaderName` | `string` | "Legacy Shaders/Transparent/Diffuse" | `pickableShader`が未設定のときに探すシェーダー名。 / 表示条件: `showAllSettings.boolValue \|\| showGrabPhysicalObjectsSettings.boolValue && grabObjectsPhysicallyEnabled.boolValue` |

### Outline Shader Device Found Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Object To Grab Found Shader | `useObjectToGrabFoundShader` | `bool` | – | 掴める対象を見つけたときにアウトラインを表示する。 / 表示条件: `showAllSettings.boolValue \|\| showOutlineShaderSettings.boolValue` |
| Object To Grab Found Shader | `objectToGrabFoundShader` | `Shader` | – | 見つけた対象に適用するアウトラインシェーダー。 / 表示条件: `showAllSettings.boolValue \|\| showOutlineShaderSettings.boolValue && useObjectToGrabFoundShader.boolValue` |
| Shader Outline Width | `shaderOutlineWidth` | `float` | – | アウトライン表示の線の太さ。 / 表示条件: `showAllSettings.boolValue \|\| showOutlineShaderSettings.boolValue && useObjectToGrabFoundShader.boolValue` |
| Shader Outline Color | `shaderOutlineColor` | `Color` | – | 見つけた対象のアウトライン色。 / 表示条件: `showAllSettings.boolValue \|\| showOutlineShaderSettings.boolValue && useObjectToGrabFoundShader.boolValue` |

### Grabbed Object Transparency Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Enable Transparency | `enableTransparency` | `bool` | true | 保持中のオブジェクトを半透明にする。 / 表示条件: `showAllSettings.boolValue \|\| showOutlineShaderSettings.boolValue` |
| Alpha Transparency | `alphaTransparency` | `float` | 0.5f | 半透明にするときのアルファ値。 / 表示条件: `showAllSettings.boolValue \|\| showOutlineShaderSettings.boolValue` |

### Drop Object Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Check If Drop Object | `useEventOnCheckIfDropObject` | `bool` | – | `checkIfDropObject`の呼び出し時にイベントを実行する。 / 表示条件: `showAllSettings.boolValue \|\| showEventsSettings.boolValue` |
| Event On Check If Drop Object | `eventOnCheckIfDropObject` | `eventParameters.eventToCallWithGameObject` | – | 対象オブジェクトを引数に渡すイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventsSettings.boolValue && useEventOnCheckIfDropObject.boolValue` |

### Remove Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Event On Objects Found | `useRemoteEventOnObjectsFound` | `bool` | – | 掴む/離す時に`remoteEventSystem`のイベントを呼ぶ。 / 表示条件: `showAllSettings.boolValue \|\| showEventsSettings.boolValue` |

### Drop Objects On Death Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Drop Current Object On Death Enabled | `dropCurrentObjectOnDeathEnabled` | `bool` | true | 死亡時に保持中のオブジェクトを落とす。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |
| Keep Melee Weapon On Death Enabled | `keepMeleeWeaponOnDeathEnabled` | `bool` | – | 死亡時も近接武器は落とさず保持する。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |

### Collision Noises Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Launched Objects Can Make Noise | `launchedObjectsCanMakeNoise` | `bool` | – | 投げたオブジェクトの衝突でノイズを発生させる。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |
| Min Object Speed To Activate Noise | `minObjectSpeedToActivateNoise` | `float` | – | ノイズを発生させる最小の投擲速度。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue && launchedObjectsCanMakeNoise.boolValue` |

### Rotation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object Can Be Rotated | `objectCanBeRotated` | `bool` | – | 保持中にマウスでオブジェクトを回転できる。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |
| Rotation Speed | `rotationSpeed` | `float` | – | オブジェクトをカメラの向きへ合わせる補間速度。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |
| Rotate Speed | `rotateSpeed` | `float` | – | マウス入力でオブジェクトを回転させる速さ。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |
| Rotate To Camera In Fixed Position | `rotateToCameraInFixedPosition` | `bool` | – | 固定位置グラブ時にカメラの向きへ自動で合わせる。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue && grabInFixedPosition.boolValue` |
| Rotate To Camera In Free Position | `rotateToCameraInFreePosition` | `bool` | – | 自由位置グラブ時にカメラの向きへ自動で合わせる。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |

### Throw Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Min Time To Increase Throw Force | `minTimeToIncreaseThrowForce` | `float` | 300 | 投げ力のチャージが成立するまでの閾値。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |
| Increase Throw Force Speed | `increaseThrowForceSpeed` | `float` | 1500 | 1秒あたりに増える投げ力の量。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |
| Extra Thorw Force | `extraThorwForce` | `float` | 10 | 投擲時に加算する追加の力の値。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |
| Max Throw Force | `maxThrowForce` | `float` | 3500 | チャージできる投げ力の上限。`powerSlider`の最大値にもなる。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |
| Take Object Mass Into Account On Throw Enabled | `takeObjectMassIntoAccountOnThrowEnabled` | `bool` | – | 質量で割って投げ力を計算する。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |
| Object Mass Divider On Throw | `objectMassDividerOnThrow` | `float` | 1 | 投げ力計算で質量に掛ける除数。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue && takeObjectMassIntoAccountOnThrowEnabled.boolValue` |
| Head Track Body Weight On Aim | `headTrackBodyWeightOnAim` | `float` | 1 | エイム時に頭トラッキングへ渡す体の重み。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |
| Custom Aim Reticle Name | `customAimReticleName` | `string` | "Reticle 1" | エイム時に表示するカスタムレティクル名。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |
| Ignore Throw Animation For Physical Objects | `ignoreThrowAnimationForPhysicalObjects` | `bool` | – | 物理オブジェクトの投げアニメーションを再生しない。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |
| Ignore Throw Animation For Melee Physical Objects | `ignoreThrowAnimationForMeleePhysicalObjects` | `bool` | – | 近接武器の投げアニメーションを再生しない。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |

### Zoom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Use Zoom While Grabbed | `canUseZoomWhileGrabbed` | `bool` | – | 保持中にホイールで距離をズームできる。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |
| Zoom Speed | `zoomSpeed` | `float` | – | ズームで保持距離が変わる速さ。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |
| Max Zoom Distance | `maxZoomDistance` | `float` | – | ズームで遠ざけられる最大の保持距離。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |
| Min Zoom Distance | `minZoomDistance` | `float` | – | ズームで近づけられる最小の保持距離。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |

### Power Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Layer | `layer` | `LayerMask` | – | 掴む対象を探すレイキャストのレイヤーマスク。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |
| Gravity Objects Layer | `gravityObjectsLayer` | `LayerMask` | – | 重力操作時に接地判定するレイヤーマスク。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |
| Layer For Custom Gravity Object | `layerForCustomGravityObject` | `string` | – | 重力操作中にオブジェクトへ設定するレイヤー名。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |
| Power Force Mode | `powerForceMode` | `ForceMode` | – | 投擲時に使う`ForceMode`。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |
| Use Throw Objects Layer | `useThrowObjectsLayer` | `bool` | true | 照準先のサーフェスへ向けて投げる。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |
| Throw Objects Layer To Check | `throwObjectsLayerToCheck` | `LayerMask` | – | 投擲方向を決めるレイキャストのレイヤーマスク。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |
| Use Grabbed Particles | `useGrabbedParticles` | `bool` | – | 保持中に煙パーティクルを出す。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |
| Use Load Throw Particles | `useLoadThrowParticles` | `bool` | – | チャージ中と発射時にパーティクルを出す。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |

### Realistic Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Throw Power | `throwPower` | `float` | – | `realistic`モードで質量に掛ける投擲力。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |
| Realistic Force Mode | `realisticForceMode` | `ForceMode` | – | `realistic`モードの投擲に使う`ForceMode`。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |

### AI Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Used By AI | `usedByAI` | `bool` | – | AIが操作する場合は更新処理を行わない。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |

### UI Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Cursor | `useCursor` | `bool` | true | 照準カーソルを表示・制御する。 / 表示条件: `showAllSettings.boolValue \|\| showUISettings.boolValue` |
| Grab Object Action Name | `grabObjectActionName` | `string` | "Grab Object" | キー表示に使う入力アクション名。 / 表示条件: `showAllSettings.boolValue \|\| showUISettings.boolValue` |
| Extra Text Start Action Key | `extraTextStartActionKey` | `string` | "[" | キー表示の前に付ける装飾文字。 / 表示条件: `showAllSettings.boolValue \|\| showUISettings.boolValue` |
| Extra Text End Action Key | `extraTextEndActionKey` | `string` | "]" | キー表示の後に付ける装飾文字。 / 表示条件: `showAllSettings.boolValue \|\| showUISettings.boolValue` |
| Touch Button Icon | `touchButtonIcon` | `GameObject` | – | タッチ操作時にキー文字の代わりに出すアイコン。 / 表示条件: `showAllSettings.boolValue \|\| showUISettings.boolValue` |
| Show Object To Grab Name Enabled | `showObjectToGrabNameEnabled` | `bool` | – | 掴めるオブジェクトの名前パネルを表示する。 / 表示条件: `showAllSettings.boolValue \|\| showUISettings.boolValue` |
| Object To Grab Name Text | `objectToGrabNameText` | `Text` | – | オブジェクト名を表示するテキスト。 / 表示条件: `showAllSettings.boolValue \|\| showUISettings.boolValue && showObjectToGrabNameEnabled.boolValue` |
| Object To Grab Name Panel | `objectToGrabNamePanel` | `GameObject` | – | オブジェクト名を表示するパネル。 / 表示条件: `showAllSettings.boolValue \|\| showUISettings.boolValue && showObjectToGrabNameEnabled.boolValue` |

### Player State

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Object Held | `objectHeld` | `GameObject` | – | 現在保持しているオブジェクト。実行時の状態。 / 表示条件: `showAllSettings.boolValue \|\| showDebugSettings.boolValue && objectHeld.objectReferenceValue` |
| Current Physical Object To Grab Found | `currentPhysicalObjectToGrabFound` | `GameObject` | – | 物理的に掴める対象として検出中のオブジェクト。 / 表示条件: `showAllSettings.boolValue \|\| showDebugSettings.boolValue` |
| Current Object To Grab Found | `currentObjectToGrabFound` | `GameObject` | – | レイキャストで検出した最後のオブジェクト。 / 表示条件: `showAllSettings.boolValue \|\| showDebugSettings.boolValue` |

### Grab Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Grab Zone Transform | `grabZoneTransform` | `Transform` | – | グラブエフェクトやパーティクルの発生位置。 / 表示条件: `showComponents` がオンのとき |
| Cursor | `cursor` | `GameObject` | – | 照準カーソルのGameObject。 / 表示条件: `showComponents` がオンのとき |
| Cursor Rect Transform | `cursorRectTransform` | `RectTransform` | – | カーソルのRectTransform。位置の制御に使う。 / 表示条件: `showComponents` がオンのとき |
| Found Object To Grab Cursor | `foundObjectToGrabCursor` | `GameObject` | – | 掴める対象を見つけたときに出すカーソル。 / 表示条件: `showComponents` がオンのとき |
| Grabbed Object Cursor | `grabbedObjectCursor` | `GameObject` | – | 保持中に表示する専用カーソル。 / 表示条件: `showComponents` がオンのとき |
| Power Slider | `powerSlider` | `Slider` | – | 投げ力のチャージ量を示すスライダー。 / 表示条件: `showComponents` がオンのとき |
| Grabbed Object Clonned Collider Transform | `grabbedObjectClonnedColliderTransform` | `Transform` | – | 保持中のオブジェクトに追従するコライダー用Transform。 / 表示条件: `showComponents` がオンのとき |
| Grabbed Object Clonned Collider | `grabbedObjectClonnedCollider` | `BoxCollider` | – | 保持中に使うクローンBoxCollider。衝突制御に使う。 / 表示条件: `showComponents` がオンのとき |

### Player Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Camera Transform | `playerCameraTransform` | `GameObject` | – | プレイヤーカメラのGameObject参照。 / 表示条件: `showComponents` がオンのとき |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | プレイヤーコントローラー参照。 / 表示条件: `showComponents` がオンのとき |
| Powers Manager | `powersManager` | `otherPowers` | – | パワー管理参照。エイムモードの解除に使う。 / 表示条件: `showComponents` がオンのとき |
| Player Input | `playerInput` | `playerInputManager` | – | 入力管理参照。マウス軸やキー名の取得に使う。 / 表示条件: `showComponents` がオンのとき |
| Player Camera Manager | `playerCameraManager` | `playerCamera` | – | カメラ管理参照。視点の判定に使う。 / 表示条件: `showComponents` がオンのとき |
| Using Devices Manager | `usingDevicesManager` | `usingDevicesSystem` | – | デバイス使用管理参照。アウトライン解除の判定に使う。 / 表示条件: `showComponents` がオンのとき |
| Weapons Manager | `weaponsManager` | `playerWeaponsManager` | – | 武器管理参照。物理保持中は武器をしまう。 / 表示条件: `showComponents` がオンのとき |
| Gravity Manager | `gravityManager` | `gravitySystem` | – | 重力管理参照。重力室の判定に使う。 / 表示条件: `showComponents` がオンのとき |
| IK Manager | `IKManager` | `IKSystem` | – | IK管理参照。手のマウントポイント取得に使う。 / 表示条件: `showComponents` がオンのとき |
| Main Collider | `mainCollider` | `Collider` | – | プレイヤーのメインコライダー。保持物との衝突を無視する。 / 表示条件: `showComponents` がオンのとき |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | メインカメラのTransform。レイキャストや保持位置の基準。 / 表示条件: `showComponents` がオンのとき |
| Main Camera | `mainCamera` | `Camera` | – | メインカメラ。画面座標への変換に使う。 / 表示条件: `showComponents` がオンのとき |
| High Friction Material | `highFrictionMaterial` | `PhysicsMaterial` | – | 重力操作時に付ける高摩擦のPhysicMaterial。 / 表示条件: `showComponents` がオンのとき |
| Main Grabbed Object Melee Attack System | `mainGrabbedObjectMeleeAttackSystem` | `grabbedObjectMeleeAttackSystem` | – | 近接武器の保持を扱うシステム参照。 / 表示条件: `showComponents` がオンのとき |
| Main Head Track | `mainHeadTrack` | `headTrack` | – | 頭トラッキング参照。エイム時の重み設定に使う。 / 表示条件: `showComponents` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `particles` | `GameObject []` | – | – |
| `grabbed` | `bool` | – | – |
| `gear` | `bool` | – | – |
| `rail` | `bool` | – | – |
| `regularObject` | `bool` | – | – |
| `ableToGrabTags` | `List<string>` | new List<string> () | – |
| `handInfoList` | `List<handInfo>` | new List<handInfo> () | – |
| `carryingPhysicalObject` | `bool` | – | – |
| `currentPhysicalObjectGrabbed` | `GameObject` | – | – |
| `currentPhysicsObjectElement` | `GameObject` | – | – |
| `physicalObjectToGrabFoundList` | `List<GameObject>` | new List<GameObject> () | – |
| `objectFocus` | `bool` | – | – |
| `remoteEventNameListOnGrabObject` | `List<string>` | new List<string> () | – |
| `remoteEventNameListOnDropObject` | `List<string>` | new List<string> () | – |
| `aiming` | `bool` | false | – |
| `showComponents` | `bool` | – | – |
| `objectIsVehicle` | `bool` | – | – |
| `grabObjectsInputPaused` | `bool` | – | – |
| `showStrengthSettings` | `bool` | – | – |
| `showGrabPhysicalObjectsSettings` | `bool` | – | – |
| `showOutlineShaderSettings` | `bool` | – | – |
| `showEventsSettings` | `bool` | – | – |
| `showOtherSettings` | `bool` | – | – |
| `showDebugSettings` | `bool` | – | – |
| `showAllSettings` | `bool` | – | – |
| `showUISettings` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkDisableWeightPanel()` | 無限筋力でなく重量表示が有効なとき、重量パネルを非表示にして`weigthPanelActive`を`false`にする。 |
| `checkObjectWeight(GameObject objectToCheck)` | 対象の`grabObjectProperties`から重量を取得し、重量パネルの表示・数値・重すぎる場合の文字色を更新する。 |
| `enableOrDisableIconButton(bool state)` | アイコン配置時のみ`grabObjectIcon`の表示を`state`に合わせ、有効フラグも更新する。 |
| `grabObject()` | 検出済みの物理オブジェクト、またはカメラ前方の`Raycast`結果を`grabCurrenObject`へ渡して掴む。 |
| `grabPhysicalObjectExternally(GameObject objectToGrab)` | 対象を検出オブジェクトに設定してから`grabCurrenObject`を呼ぶ。 |
| `grabCurrenObject(GameObject objectToGrab)` | タグ・重量・IKなどを検証し、タグとレイヤを退避して掴み状態を設定、物理持ち上げや各イベント呼び出しまで行う。 |
| `checkTypeObject(GameObject objectToCheck)` | `ableToGrabTags`や車両、`grabObjectParent`を持つ対象を掴めると判定して返す。 |
| `checkToDropObjectIfNotPhysicalWeaponElseKeepWeapon()` | 近接武器を所持中なら武器保持を確認し、そうでなければ`dropObject`で落とす。 |
| `checkToDropObjectIfCarryingRegularPhysicalObject()` | 物理オブジェクトを運搬中でかつ近接武器を所持していない場合のみ`dropObject`で落とす。 |
| `setIgnoreDropMeleeWeaponOnDeathState(bool state)` | 死亡時に近接武器を落とさないフラグ`ignoreDropMeleeWeaponOnDeath`を設定するだけ。 |
| `checkToDropObjectOnDeath()` | 死亡時設定が有効なら、武器保持設定に応じて武器以外のみ落とすか`dropObject`する。 |
| `dropObject()` | 投擲方向を算出したうえでタグ・レイヤ・重力・透明化・物理運搬・各イベントを復元し、掴み状態を解除する。 |
| `checkJointsInObject(GameObject objectToThrow, float force)` | 関節があれば接続先へ再帰し、なければ`addForceToThrownRigidbody`で`force`を加える。 |
| `addForceToThrownRigidbody(GameObject objectToThrow, float force)` | 子の非キネマティックな`Rigidbody`へ質量と`force`に応じた力を加え、速度に応じて衝突ノイズを有効化する。 |
| `getLastHoldTimer()` | 溜め時間`holdTimer`を返すだけ。 |
| `getThrowDirection()` | カメラ前方のレイで表面方向を求め、`throwObjectDirection`に保存して返す。 |
| `checkGrabbedObjectAction()` | `powers`では重力変更用に落として重力制御を付与し、`realistic`では現実投擲を呼ぶ。 |
| `throwRealisticGrabbedObject()` | パワースライダーを消し、`dropObject`後に質量×`throwPower`の力をカメラ前方へ加えてノイズ判定も行う。 |
| `changeGrabbedZoom(int zoomType)` | リセットを止め`zoomType`の符号で`holdDistance`を増減し、位置方式ごとに制限する。 |
| `resetFixedGrabedTransformPosition()` | 固定位置で掴み中なら、位置と`holdDistance`を戻すコルーチンを開始する。 |
| `stopResetFixedGrabedTransformPositionCoroutine()` | 実行中のリセットコルーチンを停止するだけ。 |
| `enableOrDisableGrabObjectCursor(bool value)` | `false`のときのみ`cursorRectTransform`の`localPosition`をゼロに戻す。 |
| `enableOrDisableGeneralCursor(bool state)` | `useCursor`が有効なとき、`cursor`の表示を`state`に合わせる。 |
| `enableOrDisableGeneralCursorFromExternalComponent(bool state)` | `enableOrDisableGeneralCursor`をそのまま呼ぶだけ。 |
| `enableOrDisableFoundObjectToGrabCursor(bool state)` | `foundObjectToGrabCursor`の表示を`state`に合わせる。 |
| `checkIfDropObject(GameObject objectToCheck)` | 指定物を掴んでいれば`dropObject`し、設定時は`eventOnCheckIfDropObject`を発火する。 |
| `checkIfObjectCanBePlaced(GameObject objectToCheck)` | 指定オブジェクトを掴んでいても物理運搬中なら`false`を返し、それ以外は`true`を返す。 |
| `checkIfDropObject()` | `objectHeld`が無いか物理オブジェクトを保持中なら`dropObject`で落とす。 |
| `setAimingState(bool state)` | `aiming`を更新して掴みカーソルを切り替え、解除時は前オブジェクトのシェーダも元に戻す。 |
| `getGrabbedObject()` | 掴み中の`objectHeld`を返すだけ。 |
| `isGrabbedObject()` | `objectHeld`が`null`でないかを返すだけ。 |
| `checkIfEnableNoiseOnCollision(GameObject objectToCheck, float launchSpeed)` | `launchSpeed`が閾値以上なら、対象の`noiseSystem`でノイズ使用を有効化する。 |
| `addForceToLaunchObject()` | 溜め中に`holdTimer`とパワースライダーを増加させ、一定時間を超えるとスライダーやパーティクルを表示する。 |
| `launchObject()` | `dropObject`後に溜め時間に応じた力を加え、投擲アニメーションや`launchedObjects`も扱う。 |
| `isCurrentObjectToGrabFound(GameObject objectToCheck)` | 通常・物理それぞれの検出オブジェクトのいずれかと一致すれば`true`を返す。 |
| `objectInphysicalObjectToGrabFoundList(GameObject objectToCheck)` | `physicalObjectToGrabFoundList`に含まれるかどうかを返すだけ。 |
| `addCurrentPhysicalObjectToGrabFound(GameObject objectToGrab)` | 未登録ならリストへ追加し、`elementsOnPhysicalObjectsFoundList`を`true`にする。 |
| `removeCurrentPhysicalObjectToGrabFound(GameObject objectToGrab)` | リストから削除し、空になったらシェーダ復元・検出オブジェクト消去・重量パネル非表示まで行う。 |
| `clearPhysicalObjectToGrabFoundList()` | 検出リストを空にし、シェーダ復元と現在の検出オブジェクト・重量パネルの解除をまとめて行う。 |
| `physicalObjectToGrabFound()` | `currentPhysicalObjectToGrabFound`が存在するかどうかを返すだけ。 |
| `getClosestPhysicalObjectToGrab()` | 運搬中は-1を返し、それ以外は画面中心や距離で最近傍を選んで検出オブジェクトを更新し、その添字を返す。 |
| `checkIfSetNewShaderToObjectToGrabFound(GameObject objectToCheck)` | シェーダ設定が有効なら、対象の`outlineObjectSystem`に検出用のアウトラインを適用する。 |
| `checkIfSetOriginalShaderToPreviousObjectToGrabFound()` | 設定が有効なら前オブジェクトのアウトラインを解除し、保持参照も`null`にする。 |
| `setKeyText(bool state)` | タッチ時はボタンアイコンへ切り替え、非タッチ時は掴みキー表記を設定、名前パネルも更新する。 |
| `isIKSystemEnabledOnCurrentGrabbedObject()` | `IKSystemEnabledOnCurrentGrabbedObject`を返すだけ。 |
| `grabPhysicalObject(grabPhysicalObjectSystem.grabPhysicalObjectInfo newGrabPhysicalObjectInfo)` | アクティブならコルーチン経由、そうでなければ直接`grabPhysicalObjectDirectly`を呼ぶ。 |
| `setGrabbedObjectClonnedColliderEnabledState(bool state)` | `true`なら0.6秒待ってから有効化するコルーチンを開始し、`false`なら即座に無効化する。 |
| `dropPhysicalObject()` | 移動やコルーチンを止め、歩行速度・入力制限・スケール・IK・コライダ衝突を復元して運搬状態を解除する。 |
| `isCarryingPhysicalObject()` | `carryingPhysicalObject`を返すだけ。 |
| `getCurrentPhysicalObjectGrabbed()` | `currentPhysicalObjectGrabbed`を返すだけ。 |
| `translatePhysicalObject(Vector3 worldPosition)` | 既存の移動を止め、`worldPosition`へ向かう移動コルーチンを開始する。 |
| `stopTranslatePhysicalObject()` | 実行中の運搬移動コルーチンを停止するだけ。 |
| `checkPhysicalObjectGrabbedPosition(bool firstPersonActive)` | 視点に応じて親や参照位置を選び直し、運搬中オブジェクトの親・ローカル位置回転・透明化を更新する。 |
| `checkIfDropObjectIfNotPhysical(bool disableAimState)` | `disableAimState`ならエイムを解除し、物理運搬中でなければ`dropObject`する。 |
| `checkIfDropObjectIfPhysical()` | 物理オブジェクトを運搬中の場合のみ`dropObject`で落とす。 |
| `isPauseCameraMouseWheelWhileObjectGrabbedActive()` | `pauseCameraMouseWheelWhileObjectGrabbed`を返すだけ。 |
| `setGrabObjectsEnabledState(bool state)` | `grabObjectsEnabled`を設定するだけ。 |
| `isGrabObjectsEnabled()` | `grabObjectsEnabled`を返すだけ。 |
| `setGrabObjectsPhysicallyEnabledState(bool state)` | `grabObjectsPhysicallyEnabled`を設定するだけ。 |
| `isGrabObjectsPhysicallyEnabled()` | `grabObjectsPhysicallyEnabled`を返すだけ。 |
| `setGrabObjectsInputPausedState(bool state)` | `grabObjectsInputPaused`を設定するだけ。 |
| `setGrabObjectsInputDisabledState(bool state)` | `grabObjectsInputDisabled`を設定するだけ。 |
| `isCarryingMeleeWeapon()` | 近接武器システムがあれば`isCarryingObject`の結果を返し、なければ`false`を返す。 |
| `isCarryingRegularPhysicalObject()` | 物理運搬中でかつ近接武器を所持していない場合のみ`true`を返す。 |
| `activateReturnProjectilesOnContact()` | 近接武器システムがあれば`activateReturnProjectilesOnContact`を呼ぶだけ。 |
| `keepOrCarryGrabbebObject(bool keepGrabbedObject)` | 掴み中かつ物理運搬中に保持状態を設定し、`checkPhysicalObjectGrabbedPosition`で補正する。 |
| `isFirstPersonActive()` | `playerCameraManager.isFirstPersonActive`を返すだけ。 |
| `setCurrentGrabObjectGenericModeMountPointSystem(grabObjectGenericModeMountPointSystem newGrabObjectGenericModeMountPointSystem)` | マウントポイントシステムを設定し、`null`でないかを割り当て済みフラグへ反映する。 |
| `inputGrabObject()` | 入力停止・無効などの条件を確認し、エイム中か検出物があれば`grabObject`を呼んで最終入力時刻を記録する。 |
| `inputHoldToLaunchObject()` | 掴み直後の0.3秒を除いて`holdingLaunchInputActive`を立て、3D移動と自由カメラの状態を記録する。 |
| `inputReleaseToLaunchObject()` | 溜め入力を解除し、条件を満たせば投擲アニメーションのコルーチンか`launchObject`を呼ぶ。 |
| `inputSetRotateObjectState(bool rotationEnabled)` | 回転可能な通常物を掴み中なら、カメラ回転を止め`rotatingObject`を設定する。 |
| `inputZoomObject(bool zoomIn)` | ズーム許可時に`zoomIn`に応じ`changeGrabbedZoom`を±1で呼ぶ。 |
| `inputResetFixedGrabedTransformPosition()` | 回転可能な通常物を掴み中なら`resetFixedGrabedTransformPosition`を呼ぶ。 |
| `initializeStrengthAmount(float newValue)` | `strengthAmount`を`newValue`で初期化するだけ。 |
| `increaseStrengthAmount(float newValue)` | `strengthAmount`に`newValue`を加算するだけ。 |
| `updateStrengthAmountWithoutUpdatingStatManager(int statId, float amount)` | 統計を更新せず`strengthAmount`を`amount`にするだけ。 |
| `increaseStrengthAmountAndUpdateStat(float newValue)` | 筋力を加算し、`playerStatsManager`があれば対応する統計値も更新する。 |
| `setUseInfiniteStrengthState(bool state)` | `useInfiniteStrength`を設定するだけ。 |
| `setUsedByAIState(bool state)` | `usedByAI`を設定するだけ。 |
| `setUseObjectToGrabFoundShaderState(bool state)` | `useObjectToGrabFoundShader`を設定するだけ。 |
| `setUseObjectToGrabFoundShaderStateFromEditor(bool state)` | 検出オブジェクトのシェーダ設定を変更してから`updateComponent`で反映する。 |
| `setGrabObjectsEnabledStateFromEditor(bool state)` | 有効状態を変更してから`updateComponent`で反映する。 |
| `updateComponent()` | `GKC_Utils.updateComponent`とシーン更新を呼び、プレイヤーカリングを更新させる。 |

## 内部型

- `grabMode`（enum）
- `handInfo`（class）
