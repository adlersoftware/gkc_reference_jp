# Localization System メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Localization System/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **14 型 / 50 メソッド**
- 注釈付き: **50 メソッド**（100%）
- 生成元: 各 `.cs` の実装。多言語テーブルとキー解決。

## （直下）

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`gameLanguageSelector`](reference/Localization%20System/gameLanguageSelector.md) | ゲーム全体の現在言語を管理するシングルトンで、言語変更時に各ローカライズ管理とシーン内の要素表示をまとめて更新する。PlayerPrefsへの保存や起動時のシステム言語チェックも担う。 | 17/17 |
| [`languageLocalizationManager`](reference/Localization%20System/languageLocalizationManager.md) | 各ローカライズ管理コンポーネントの基底クラスで、ファイルパスの解決や言語ファイルの存在確認、言語変更イベントを提供する。編集・辞書取得系は継承先で実装する仮想メソッド。 | 14/14 |
| [`localizationFileLoader`](reference/Localization%20System/localizationFileLoader.md) | CSV形式のローカライズファイルを読み書きするローダーで、言語列を辞書化し、キーや言語の追加削除をエディタ上で行う。 | 6/6 |
| [`simpleGameLanguageSelector`](reference/Localization%20System/simpleGameLanguageSelector.md) | メインの`gameLanguageSelector`を探して言語設定を委譲する簡易セレクタで、変更時にドロップダウン更新と独自イベントを行う。 | 2/2 |
| [`languageElementChecker`](reference/Localization%20System/languageElementChecker.md) | UI要素などに言語ごとのテキストを持たせ、言語変更時に表示を切り替えるための基底コンポーネント。 | 2/2 |
| [`UIElementsLocalizationManager`](reference/Localization%20System/UIElementsLocalizationManager.md) | UI要素用のローカライズファイルを読み込み、キーから翻訳値を返す静的マネージャー。 | 1/1 |
| [`interactionObjectsLocalizationManager`](reference/Localization%20System/interactionObjectsLocalizationManager.md) | インタラクト対象（装置名など）用のローカライズを読み込み、キーから翻訳値を返す静的マネージャー。 | 1/1 |
| [`inventoryLocalizationManager`](reference/Localization%20System/inventoryLocalizationManager.md) | インベントリ用のローカライズを読み込み、キーから翻訳値を返す静的マネージャー。 | 1/1 |
| [`missionLocalizationManager`](reference/Localization%20System/missionLocalizationManager.md) | ミッション用のローカライズを読み込み、キーから翻訳値を返す静的マネージャー。 | 1/1 |
| [`pointAndClickLocalizationManager`](reference/Localization%20System/pointAndClickLocalizationManager.md) | ポイント＆クリック用のローカライズを読み込み、キーから翻訳値を返す静的マネージャー。 | 1/1 |
| [`skillsLocalizationManager`](reference/Localization%20System/skillsLocalizationManager.md) | スキル用のローカライズを読み込み、キーから翻訳値を返す静的マネージャー。 | 1/1 |
| [`searcherLocalizationToolEditor`](reference/Localization%20System/searcherLocalizationToolEditor.md) | ローカライズのキーを検索し、削除や新規追加を行えるエディタウィンドウ。 | 1/1 |
| [`addKeyLocalizationToolEditor`](reference/Localization%20System/addKeyLocalizationToolEditor.md) | 指定言語へ新しいキーと値を追加するエディタウィンドウ。 | 1/1 |
| [`addLanguageLocalizationToolEditor`](reference/Localization%20System/addLanguageLocalizationToolEditor.md) | ローカライズファイルへ新しい言語列を追加するエディタウィンドウ。 | 1/1 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- 状態遷移・イベント発火・UI 更新・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

