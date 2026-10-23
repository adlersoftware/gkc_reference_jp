# hologramDoor

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/hologramDoor.cs:8`

**概要**: `doorSystem` の手前に置くホログラム制御で、トリガーへの入退場とタグ判定で扉を開閉する。テキスト・色・透明度・効果音・`eventOnOpen` で施錠／解錠の見た目を演出する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Unlocked Text | `unlockedText` | `string` | – | – |
| Locked Text | `lockedText` | `string` | – | – |
| Open Text | `openText` | `string` | – | – |
| Hologram Idle | `hologramIdle` | `string` | – | – |
| Hologram Inside | `hologramInside` | `string` | – | – |
| Fade Hologram Speed | `fadeHologramSpeed` | `float` | 4 | – |
| Open Delay | `openDelay` | `float` | – | – |
| Locked Color | `lockedColor` | `Color` | – | – |
| Door To Open | `doorToOpen` | `GameObject` | – | – |
| Open On Trigger | `openOnTrigger` | `bool` | – | – |
| Tag List To Open | `tagListToOpen` | `List<string>` | new List<string> () | – |

### Sounds Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Enter Sound | `enterSound` | `AudioClip` | – | – |
| Enter Audio Element | `enterAudioElement` | `AudioElement` | – | – |
| Exit Sound | `exitSound` | `AudioClip` | – | – |
| Exit Audio Element | `exitAudioElement` | `AudioElement` | – | – |
| Locked Sound | `lockedSound` | `AudioClip` | – | – |
| Locked Audio Element | `lockedAudioElement` | `AudioElement` | – | – |
| Open Sound | `openSound` | `AudioClip` | – | – |
| Open Audio Element | `openAudioElement` | `AudioElement` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Open | `useEventOnOpen` | `bool` | – | – |
| Event On Open | `eventOnOpen` | `UnityEvent` | – | – |

### Hologram Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Hologram Text | `hologramText` | `List<Text>` | new List<Text> () | – |
| Holograms | `holograms` | `List<GameObject>` | new List<GameObject> () | – |
| Hologram Central Ring | `hologramCentralRing` | `List<GameObject>` | new List<GameObject> () | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Door Manager | `doorManager` | `doorSystem` | – | – |
| Audio Source | `audioSource` | `AudioSource` | – | – |
| Door Locked | `doorLocked` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateDevice()` | `openCurrentDoor` を呼び、開扉要求を委譲するだけ。 |
| `openCurrentDoor()` | 解錠済みで閉扉・非移動・非占有なら開扉音とフェードを開始し、開扉コルーチンと `eventOnOpen` を実行する。 |
| `startChangeTransparencyCoroutine(bool state)` | 色変更とフェードのコルーチンを止め、`state` 用の透明度フェードを開始する。 |
| `stopChangeTransparency()` | `changeTransparencyCoroutine` を停止してフェードを中断するだけ。 |
| `setHologramTransparencyAtOnce(bool state)` | `state` が true ならアルファを -1 で非表示、false なら 1 で表示に即時設定する。 |
| `startSetHologramColorsCoroutine(bool useUnlockedColors)` | 色変更コルーチンを停止し、`useUnlockedColors` で元色か施錠色を選んで開始する。 |
| `stopSetHologramColors()` | `setHologramColorsCoroutine` を停止し色の補間を打ち切るだけ。 |
| `unlockHologram()` | `doorLocked` を false にし解除テキストへ変えて、元色へ戻す色変更を開始する。 |
| `lockHologram()` | `doorLocked` を true にし施錠テキストへ変えて、`lockedColor` への色変更を開始する。 |
| `startOpenDoorCoroutine()` | 開扉コルーチンを止め、`openDelay` 待機後に扉を開く `openDoor` を開始する。 |
| `stopOpenDoor()` | `openDoorCoroutine` を停止し開扉待ちをキャンセルするだけ。 |
| `checkTriggerInfo(Collider col, bool isEnter)` | タグが `tagListToOpen` にある場合のみ、`isEnter` で入場／退場処理を呼び分ける。 |
| `enteringDoor()` | 解錠なら開扉テキストにし `inside` を立て、扉停止中は施錠音か入場音、`openOnTrigger` なら開扉する。 |
| `exitingDoor()` | 開閉無効なら中断し、通常テキストへ戻して `inside` を解除、リング演出を逆再生して退場音を鳴らす。 |
| `checkIfTagCanOpen(string tagToCheck)` | `tagListToOpen` に `tagToCheck` が含まれるかを返すだけ。 |
| `openHologramDoorByExternalInput()` | 閉扉なら `openOnTrigger` を一時的に立てて入場処理、開扉なら退場処理と扉状態切替を行う。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnOpen` | `UnityEvent` | – |
