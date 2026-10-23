# timeBullet

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Powers/timeBullet.cs:5`

**概要**: バレットタイム（時間スローの）管理。`Time.timeScale`を書き換え、持続時間や音のピッチも扱う。

**公式ドキュメント抜粋**（[Time Bullet](../../docs/character-level-components/character/time-bullet.md)）

> 

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Time Bullet Enabled | `timeBulletEnabled` | `bool` | – | – |
| Time Bullet Time Speed | `timeBulletTimeSpeed` | `float` | 0.1f | – |
| Restore Audio Pitch | `restoreAudioPitch` | `bool` | – | – |

### Input Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Time Bullet By Input Enabled | `timeBulletByInputEnabled` | `bool` | true | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Time Bullet Time | `timeBulletTime` | `float` | 1 | – |
| Time Bullet Activated | `timeBulletActivated` | `bool` | – | – |
| Previously Activated | `previouslyActivated` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateTime()` | バレットタイムをトグルし、有効なら設定速度、解除なら1へ戻して時間スケールを更新する。 |
| `updateTimeBulletTime(float newValue)` | 時間値`timeBulletTime`を保持するだけで、実際の適用はしない。 |
| `updateTimeScaleValue()` | `Time.timeScale`と`fixedDeltaTime`を現在の時間値に反映する。 |
| `disableTimeBullet()` | バレットタイム中なら解除し、再開用フラグ`previouslyActivated`を立てる。 |
| `disableTimeBulletTotally()` | バレットタイムを解除し、再開用フラグも下ろして完全に終了させる。 |
| `reActivateTime()` | 再開フラグが立っていれば、少し待ってから再度トグルするコルーチンを開始する。 |
| `changeAudioPitch()` | `restoreAudioPitch`が有効なら、全`AudioSource`のピッチを1へ戻す。 |
| `activateTimeBulletXSeconds(float timeBulletDuration, float timeScale)` | 指定時間だけバレットタイムにするコルーチンを開始し、既存のものは停止する。 |
| `setCustomTimeBulletDuration(float timeScale)` | 引数名と異なり、カスタム継続時間`customTimeBulletDuration`を設定する。 |
| `activateTimeBulletXSeconds(float timeBulletDuration)` | カスタム継続時間でバレットタイムを一時的に有効化するコルーチンを開始する。 |
| `setBulletTimeState(bool state, float timeScale)` | 時間が停止していない場合のみ、状態と時間スケールを設定する。 |
| `setNewTimeBulletTimeSpeedValue(float newValue)` | バレットタイムの速度値を設定するだけ。 |
| `setOriginalTimeBulletTimeSpeed()` | 開始時に保存した元の速度値へ戻す。 |
| `setTimeValues(bool state, float timeScale)` | 有効時のみ再開コルーチンを止め、状態・時間値・音のピッチをまとめて更新する。 |
| `inputActivateBulletTime()` | 機能有効かつ入力許可時のみ`activateTime`を呼ぶ。 |
| `setTimeBulletByInputEnabledState(bool state)` | 入力による発動許可フラグを設定するだけ。 |
| `isTimeBulletActivated()` | バレットタイム中かどうかを返すだけ。 |
| `setTimeBulletByInputEnabledStateFromEditor(bool state)` | 入力許可フラグを設定してから、エディタ用にコンポーネントを更新する。 |
