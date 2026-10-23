# AudioManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **namespace**: `GameKitController.Audio`
- **ソース**: `Audio/AudioManager.cs:5`

**概要**: オーディオ関連のシングルトン。`Instance`を保持し、自身に付いた外部オーディオプレイヤー実装を取得する。

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `GetExternalAudioPlayer()` | 自身に付いた`IExternalAudioPlayer`実装を`GetComponent`で取得して返す。 |
