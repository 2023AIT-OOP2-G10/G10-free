from flask import Flask,jsonify
import json  # Python標準のJSONライブラリを読み込んで、データの保存等に使用する

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく

def store_json(name,score):
    try:

        # JSONファイルを開く
        with open('store.json') as f:
            json_data = json.load(f)

        # 登録するデータの形式でパラメータを設定
        item = {"name": name,"score": score,}
        
        # 開いたJSONデータに対してデータの追加
        json_data.append(item)

        # 保存処理
        with open('store.json', 'w') as f:
            # インデントや整形の設定を付加して吐き出し
            json.dump(json_data, f, 
                    ensure_ascii = False,
                    indent = 4,
                    sort_keys = True,
                    separators = (',', ': '))

    except IOError as e:
        # Tracebackの表示
        import traceback
        traceback.print_exc()

        # 例外の詳細メッセージをレスポンスで返す
        return jsonify({
            "error": f"ファイルの保存処理に失敗しました。<pre>{ e.args }</pre>"
        })

    # 戻り値データの表示のために再度開く
    with open('store.json') as f:
        json_data = json.load(f)

    # 正常終了の戻り値を返します。
    return jsonify({"json_data": json_data})