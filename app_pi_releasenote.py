
import streamlit as st

def display_release_notes():
    markdown_text = """
    # AI Assistant リリースノート

    ## V1.2.0（予定）
    - リリース日時：2023年9月〇日 16:00

    ### バージョンアップの概要
    - 校正機能のプロンプト改良
    - その他、リリースノート掲載（バージョン情報からリンク）等軽微な修正

    ### 実装されている主な機能
    - Q&A：自由に質問
    - Translation：英文の翻訳
    - Proofreading：日本語の文章の校正
    - Excel Formula Analysis：Excel関数の分析
    - VBA Analysis：VBAコードの分析
    - Data Analysis：ログデータ等の分析

    ### 今後追加開発予定の機能
    - 出力結果のコピー / ダウンロード機能
    - 質問ログ出力機能（何を質問したか）
    - ファイル読み込み機能

    ## V1.1.0
    - リリース日時：2023年9月5日 16:00

    ### バージョンアップの概要
    - トークン数カウント機能の追加（これに伴い、単語数・文字数カウント機能は削除）
    - Excel関数分析等での出力結果をインデントされた形式で表示する機能の追加
    - その他、モデル選択のボタン位置変更等軽微な修正

    ### 実装されている主な機能
    - Q&A：自由に質問
    - Translation：英文の翻訳
    - Proofreading：日本語の文章の校正
    - Excel Formula Analysis：Excel関数の分析
    - VBA Analysis：VBAコードの分析
    - Data Analysis：ログデータ等の分析

    ### 今後追加開発予定の機能
    - 出力結果のコピー / ダウンロード機能
    - 質問ログ出力機能（何を質問したか）
    - ファイル読み込み機能

    ## V1.0.0
    - リリース日時：2023年8月29日 21:00

    ### 実装されている主な機能
    - Q&A：自由に質問
    - Translation：英文の翻訳
    - Proofreading：日本語の文章の校正
    - Excel Formula Analysis：Excel関数の分析
    - VBA Analysis：VBAコードの分析
    - Data Analysis：ログデータ等の分析

    ### 実装されている補助的な機能
    - 認証機能の追加
    - 単語数・文字数カウント機能
    - Excel関数分析等での出力結果を改行された形式で表示する機能
    - システムプロンプト（各機能にあらかじめ組み込まれた命令文）の表示機能
    - ChatGPTモデル（「gpt-4」又は「gpt-3.5-turbo-16k」）の選択機能
    - パラメーター（TemperatureとTop_P）の調整機能

    ### 今後追加開発予定の機能
    - トークン数カウント機能
    - 出力結果のコピー / ダウンロード機能
    - Excel関数分析等での出力結果をインデントされた形式で表示する機能
    - 質問ログ出力機能（何を質問したか）
    - ファイル読み込み機能

    """
    st.markdown(markdown_text)

if __name__ == '__main__':
    display_release_notes()

