# Map メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Map/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **11 型 / 327 メソッド**
- 注釈付き: **327 メソッド**（100%）
- 生成元: 各 `.cs` の実装。マップ生成・表示・マップオブジェクト情報。

## （直下）

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`mapSystem`](reference/Map/mapSystem.md) | `mapUISystem`と`mapCreator`の建物・階情報を仲介し、2D/3Dマップカメラ、プレイヤーやアイコンの追従、コンパス、ズーム、建物・階の切替えをまとめて管理するMonoBehaviour。`mapObjects`に登録した各アイコンへ建物・階・`ID`・マップパーツの情報を付け、マップ表示全体の状態を一元制御する。 | 110/110 |
| [`mapCreator`](reference/Map/mapCreator.md) | 建物・階・マップパーツ・アイコン・各種トリガーをまとめて管理するマップ生成の中心コンポーネントで、各プレイヤーの`mapSystem`へ処理を中継する。 | 78/78 |
| [`mapUISystem`](reference/Map/mapUISystem.md) | マップ画面のUI部品参照を保持し、表示切替やボタン操作を`mapSystem`へ中継するコンポーネント。 | 45/45 |
| [`mapTileBuilder`](reference/Map/mapTileBuilder.md) | マップの1パーツ(部屋や区画)を表し、頂点列からタイルメッシュと押し出し3Dメッシュを生成する。有効/無効の切り替え、色設定、テキストやイベントトリガーの管理も担当する。 | 41/41 |
| [`mapObjectInformation`](reference/Map/mapObjectInformation.md) | マップ上に表示するオブジェクトのアイコン情報(種類・建物・フロア・表示設定)を保持するコンポーネント。`mapCreator`と`screenObjectivesSystem`への登録・削除や、到達イベントを扱う。 | 34/34 |
| [`mapZoneUnlocker`](reference/Map/mapZoneUnlocker.md) | 複数の建物・フロア・マップパーツの有効状態をまとめて管理するコンポーネント。`mapCreator`の情報を複製して保持し、ゾーン単位でパーツを解放する。 | 7/7 |
| [`addMapObjectInformation`](reference/Map/addMapObjectInformation.md) | 実行時に`mapObjectInformation`を追加し、マップアイコンや画面目標アイコンを登録する補助コンポーネント。`addMapIcon`が無効なら画面目標のみを追加する。 | 3/3 |
| [`quickTravelStationSystem`](reference/Map/quickTravelStationSystem.md) | ファストトラベル拠点のコンポーネント。プレイヤーを拠点位置へ移動させ、建物の切り替えや重力方向の再設定、到達イベントを行う。 | 3/3 |
| [`buildingAndFloorObjectInfoSystem`](reference/Map/buildingAndFloorObjectInfoSystem.md) | 対象`GameObject`に建物とフロアの親情報を設定するための中継コンポーネント。値を保持し、実際の処理は`mapCreator`へ委譲する。 | 3/3 |
| [`setMapOrientationSystem`](reference/Map/setMapOrientationSystem.md) | プレイヤーの`mapSystem`に対し、マップの向き(カメラ軸と基準`Transform`)を設定する小さな橋渡しコンポーネント。 | 2/2 |
| [`GKC_Triangulator_Utils`](reference/Map/GKC_Triangulator_Utils.md) | 2D多角形を三角形に分割するユーティリティクラス。マップパーツのタイルメッシュや3Dメッシュ生成で使われる。 | 1/1 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- 状態遷移・イベント発火・UI 更新・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

