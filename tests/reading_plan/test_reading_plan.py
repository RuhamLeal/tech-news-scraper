from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
from unittest.mock import Mock, patch
import pytest


@pytest.fixture
def mocked_find_news_data():
    mocked_data = Mock()
    mocked_data.return_value = [
        {
            "url": "https://blog.betrybe.com/novidades/noticia-01",
            "title": "Notícia 01",
            "timestamp": "01/01/2022",
            "writer": "Saturnino",
            "reading_time": 5,
            "summary": "Noticia",
            "category": "Aulas",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia-02",
            "title": "Notícia 02",
            "timestamp": "01/02/2022",
            "writer": "Alan W.",
            "reading_time": 6,
            "summary": "Noticia",
            "category": "Tecnologia",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia-03",
            "title": "Notícia 03",
            "timestamp": "01/03/2022",
            "writer": "F. R.",
            "reading_time": 20,
            "summary": "Noticia",
            "category": "Carreira",
        },
    ]
    return mocked_data


def test_reading_plan_group_news(mocked_find_news_data):

    expected_value = {
        "readable": [
            {
                "unfilled_time": 5,
                "chosen_news": [("Notícia 01", 5)],
            },
            {
                "unfilled_time": 4,
                "chosen_news": [("Notícia 02", 6)],
            },
        ],
        "unreadable": [("Notícia 03", 20)],
    }

    with patch.object(
        ReadingPlanService, "_db_news_proxy", mocked_find_news_data
    ):

        result = ReadingPlanService.group_news_for_available_time(10)
        assert result == expected_value

        with pytest.raises(
            ValueError,
            match="Valor 'available_time' deve ser maior que zero",
        ):
            ReadingPlanService.group_news_for_available_time(-1)
