# GKCLoadingScreenSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Menu/GKCLoadingScreenSystem.cs:8`

**概要**: 非同期シーン読み込み中のロード画面を制御し、読み込み完了後にキー入力を待ってシーンを有効化する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Scene Index To Load | `currentSceneIndexToLoad` | `int` | – | – |
| Activate Load On Start | `activateLoadOnStart` | `bool` | – | – |
| Scene To Load Async Prefs Name | `sceneToLoadAsyncPrefsName` | `string` | "SceneToLoadAsync" | – |
| Load Screen Progress Lerp Speed | `loadScreenProgressLerpSpeed` | `float` | 10 | – |
| Use Fake Load Progress | `useFakeLoadProgress` | `bool` | – | – |
| Fake Load Speed | `fakeLoadSpeed` | `float` | – | – |
| Click Anywhere Message | `clickAnywhereMessage` | `string` | "Click anywhere to start." | – |
| Loading Message | `loadingMessage` | `string` | "Loading... " | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Activate Change Of Scene On Any Key Press Down Enabled | `activateChangeOfSceneOnAnyKeyPressDownEnabled` | `bool` | true | – |
| Ignore Key Pressed Active | `ignoreKeyPressedActive` | `bool` | – | – |
| Ignore Mouse Pressed | `ignoreMousePressed` | `bool` | – | – |
| Use Circle Image Load | `useCircleImageLoad` | `bool` | true | – |
| Use Slider Load | `useSliderLoad` | `bool` | true | – |
| Use Text Load | `useTextLoad` | `bool` | true | – |
| Use Text Percentage Load | `useTextPercentageLoad` | `bool` | true | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Scene Loaded | `sceneLoaded` | `bool` | – | – |
| Show Debug Print | `showDebugPrint` | `bool` | true | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Load Complete | `useEventOnLoadComplete` | `bool` | – | – |
| Event On Load Complete | `eventOnLoadComplete` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Fill | `fill` | `Image` | – | – |
| Main Slider | `mainSlider` | `Slider` | – | – |
| Main Loading Text | `mainLoadingText` | `Text` | – | – |
| Percentege Text | `percentegeText` | `Text` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setKeyPressedState(bool state)` | シーン有効化を待つフラグ`keyPressed`を設定するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnLoadComplete` | `UnityEvent` | – |
