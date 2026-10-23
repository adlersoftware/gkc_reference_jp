# hideBodyPartOnCharacterSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/hideBodyPartOnCharacterSystem.cs:5`

**概要**: キャラクターのボーンをマウントポイント名で指定して非表示にするコンポーネントで、スケール0化・コライダー切替・バレットタイム併用・非表示リストの復元を扱う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Hide Body Part Enabled | `hideBodyPartEnabled` | `bool` | true | – |

### Time Bullet Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Time Bullet | `useTimeBullet` | `bool` | true | – |
| Time Bullet Duration | `timeBulletDuration` | `float` | 3 | – |
| Time Scale | `timeScale` | `float` | 0.2f | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Store Hidden Body Parts Enabled | `storeHiddenBodyPartsEnabled` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Body Part To Hide | `currentBodyPartToHide` | `Transform` | – | – |
| Stored Hiddent Body Parts List | `storedHiddentBodyPartsList` | `List<Transform>` | new List<Transform> () | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character Transform | `characterTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateBodyPartFromMountPoint(string mountPointPartName)` | `setActiveStateBodyPartFromMountPoint` を true で呼ぶだけ。 |
| `deactivateBodyPartFromMountPoint(string mountPointPartName)` | `setActiveStateBodyPartFromMountPoint` を false で呼ぶだけ。 |
| `setActiveStateBodyPartFromMountPoint(string mountPointPartName, bool state)` | マウントポイント名からボーンを取得してアクティブ状態を設定し、非表示時は記録リストへ追加する。 |
| `setEnabledStateColliderBodyPartFromMountPoint(string mountPointPartName)` | コライダー有効化を `setActiveStateColliderBodyPartFromMountPoint` に true で委譲するだけ。 |
| `setDisabledStateColliderBodyPartFromMountPoint(string mountPointPartName)` | コライダー無効化を同じ関数に false で委譲するだけ。 |
| `setActiveStateColliderBodyPartFromMountPoint(string mountPointPartName, bool state)` | マウントポイントのボーンにある `Collider` の有効状態を設定する。 |
| `hideBodyPartFromMountPoint(string mountPointPartName)` | マウントポイント名からボーンを取得し、`hideBodyPart` に渡す。 |
| `hideBodyPartFromMountPointWithoutBulletTimeCheck(string mountPointPartName)` | ボーンを `currentBodyPartToHide` に設定し、バレットタイムなしで縮小する。 |
| `hideBodyPart()` | `useTimeBullet` ならバレットタイムを発生させてから `setBodyPartScale` で対象を縮小する。 |
| `hideBodyPart(Transform newBodyPart)` | 対象を `currentBodyPartToHide` に設定して `hideBodyPart` を呼ぶ。 |
| `hideBodyPartWithoutBulletTimeCheck()` | `setBodyPartScale` を呼ぶだけ。 |
| `hideBodyPartWithoutBulletTimeCheck(Transform newBodyPart)` | 対象を `currentBodyPartToHide` に設定してから `setBodyPartScale` を呼ぶ。 |
| `setBodyPartScale()` | 有効時に対象ボーンの `localScale` を 0 にして非表示にし、設定に応じてリストへ記録する。 |
| `resetHiddenBodyPartsList()` | 記録した非表示ボーンのスケールと表示を元に戻し、リストを空にする。 |
| `setUseTimeBulletValue(bool state)` | `useTimeBullet` を設定するだけ。 |
| `setHideBodyPartEnabledState(bool state)` | `hideBodyPartEnabled` を設定するだけ。 |
| `setUseTimeBulletValueFromEditor(bool state)` | 値を設定したうえで `updateComponent` を呼ぶ。 |
| `setHideBodyPartEnabledStateFromEditor(bool state)` | 値を設定したうえで `updateComponent` を呼ぶ。 |
