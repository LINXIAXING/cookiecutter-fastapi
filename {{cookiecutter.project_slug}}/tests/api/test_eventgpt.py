import pytest
from fastapi.testclient import TestClient
from src import setting

complete_input_zh = {
    "event_args": ["时间", "地点", "事件主体", "事件客体", "事件影响"],
    "language": "中文",
    "data": "8月4日，2024年巴黎奥运会进入第九比赛日的争夺，本届奥运会的赛程已经过半。今日奥运赛场共产生了20枚金牌。中国体育代表团今日斩获3金3银2铜，奖牌总数来到45枚，位列奖牌榜第二。",
}

complete_input_en = {
    "event_args": ["time", "place", "person", "impact"],
    "language": "中文",
    "data": "北京时间8月5日凌晨，2024年巴黎奥运会男子4x100米混合泳接力在巴黎拉德芳斯体育馆进行，中国队将和美国队、澳大利亚队和东道主法国队等强劲的对手展开厮杀。美国队在这个项目上已经取得十连冠，是绝对的霸主。",
}


@pytest.mark.run(order=1)
@pytest.mark.parametrize(
    "data",
    [complete_input_zh, complete_input_en],
)
def test_eventgpt_complete_api(client: TestClient, data: dict):
    url = f"{setting.API_PREFIX}/v1/eventgpt/complete"
    response = client.post(url=url, json=data)
    assert response.status_code == 200
    assert response.json()["status"] == 200