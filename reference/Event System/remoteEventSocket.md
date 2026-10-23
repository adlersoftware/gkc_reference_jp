# remoteEventSocket

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Event System/remoteEventSocket.cs:5`

**概要**: `remoteEventSystem`への参照を保持し、ソケット無効時はnullを返す中継コンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Remote Event Socket Enabled | `remoteEventSocketEnabled` | `bool` | true | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Remote Event System | `mainRemoteEventSystem` | `remoteEventSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getMainRemoteEventSystem()` | ソケットが無効ならnull、有効なら`mainRemoteEventSystem`を返す。 |
| `isRemoteEventSocketEnabled()` | `remoteEventSocketEnabled`を返すだけのゲッター。 |
