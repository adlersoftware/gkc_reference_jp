# Game Manager メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Game Manager/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **6 型 / 130 メソッド**
- 注釈付き: **130 メソッド**（100%）
- 生成元: 各 `.cs` の実装。ゲーム全体の管理（ポーズ、設定、シーン、入力設定の保存）。

## （直下）

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`playerCharactersManager`](reference/Game%20Manager/playerCharactersManager.md) | シーン上のプレイヤー達をリスト管理し、生成・ID割り当て・カメラ/HUD/マップ設定・操作キャラの切替をまとめて行うマネージャー。セーブ処理も各プレイヤーの`saveGameSystem`へ中継する。 | 52/52 |
| [`gameManager`](reference/Game%20Manager/gameManager.md) | ゲーム全体の状態（ポーズ、プレイ時間、FPS上限、チャプター名、セーブパス、タッチ操作可否）を保持し、セーブ/ロードとプレイヤー構成の窓口になる。 | 43/43 |
| [`prefabsManager`](reference/Game%20Manager/prefabsManager.md) | カテゴリ別にプレハブを登録・検索し、エディタでカメラ前方のレイキャスト位置へ配置するための管理コンポーネント。 | 17/17 |
| [`mainManagerAdministrator`](reference/Game%20Manager/mainManagerAdministrator.md) | インベントリやミッションなどの各メインマネージャーのプレハブを一覧保持し、シーンへの生成・親の整理・プレハブへの反映を担う。 | 12/12 |
| [`switchCompanionSystem`](reference/Game%20Manager/switchCompanionSystem.md) | キャラクターをAI/プレイヤーへ切り替えるイベントを保持し、入力からの次キャラ切替を`playerCharactersManager`へ委譲するコンポーネント。 | 5/5 |
| [`basicSingleManager`](reference/Game%20Manager/basicSingleManager.md) | 単一インスタンス管理用の基底クラス。`getComponentInstance`を仮想メソッドとして持つだけの土台。 | 1/1 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- 状態遷移・イベント発火・UI 更新・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

