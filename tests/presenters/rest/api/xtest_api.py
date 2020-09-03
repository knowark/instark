# from pytest import raises
# import pytest
# from json import loads, dumps
# from aiohttp import web
# from instark.presenters.web.middleware import (
#     authenticate_middleware_factory)


# async def test_root(app) -> None:
#     response = await app.get('/')

#     content = await response.text()

#     assert response.status == 200
#     assert 'Serproser' in content


# async def test_root_api(app) -> None:
#     response = await app.get('/?api')
#     data = await response.text()
#     api = loads(data)

#     assert 'openapi' in api
#     assert api['info']['title'] == 'Serproser'


# # Allocations


# async def xtest_allocations_head(app, headers) -> None:
#     response = await app.head('/allocations', headers=headers)
#     count = response.headers.get('Total-Count')

#     assert int(count) == 2


# async def xtest_allocations_get(app, headers) -> None:
#     response = await app.get('/allocations', headers=headers)
#     content = await response.text()

#     assert response.status == 200

#     data_dict = loads(content)

#     assert len(data_dict) == 2
#     assert data_dict[0]['id'] == '1'


# # Employees

# async def test_employees_head(app, headers) -> None:
#     response = await app.head('/employees', headers=headers)
#     count = response.headers.get('Total-Count')

#     assert int(count) == 2


# async def test_employees_get(app, headers) -> None:
#     response = await app.get('/employees', headers=headers)
#     content = await response.text()

#     assert response.status == 200

#     data_dict = loads(content)

#     assert len(data_dict) == 2
#     assert data_dict[0]['id'] == 'ZZZ007'


# # News


# async def test_news_head(app, headers) -> None:
#     response = await app.head('/news', headers=headers)
#     count = response.headers.get('Total-Count')

#     assert int(count) == 2


# async def test_news_get(app, headers) -> None:
#     response = await app.get('/news', headers=headers)
#     content = await response.text()

#     assert response.status == 200

#     data_dict = loads(content)

#     assert len(data_dict) == 2
#     assert data_dict[0]['id'] == 'OPU123'


# async def test_news_put(app, headers) -> None:
#     news_data = dumps([{
#         "id": "006",
#         "description": "Riots"
#     }])

#     response = await app.put('/news', data=news_data, headers=headers)
#     content = await response.text()
#     assert response.status == 201


# async def test_news_delete(app, headers) -> None:
#     response = await app.delete('/news/OPU123', headers=headers)
#     content = await response.text()
#     assert response.status == 204

#     response = await app.get('/news', headers=headers)
#     data_dict = loads(await response.text())

#     assert len(data_dict) == 1


# async def test_news_delete_body(app, headers) -> None:
#     ids = dumps(["OPU123"])
#     response = await app.delete(
#         '/news', data=ids, headers=headers)
#     content = await response.text()
#     assert response.status == 204

#     response = await app.get('/news', headers=headers)
#     data_dict = loads(await response.text())

#     assert len(data_dict) == 1


# # Occurrences


# async def test_occurrences_head(app, headers) -> None:
#     response = await app.head('/occurrences', headers=headers)
#     count = response.headers.get('Total-Count')

#     assert int(count) == 5


# async def test_occurrences_get(app, headers) -> None:
#     response = await app.get('/occurrences', headers=headers)
#     content = await response.text()

#     assert response.status == 200

#     data_dict = loads(content)

#     assert len(data_dict) == 5
#     assert data_dict[0]['id'] == 'ABC123'


# async def test_occurrences_put(app, headers) -> None:
#     occurrence_data = dumps([{
#         "id": "ABCXYZ007",
#         "name": "Frank",
#         "type": "report",
#         "siteId": "001",
#         "timestamp": 1563226168,
#         "employeeId": "003"
#     }])

#     response = await app.put('/occurrences',
#                              data=occurrence_data, headers=headers)
#     content = await response.text()
#     assert response.status == 201


# # Reviews


# async def test_reviews_head(app, headers) -> None:
#     response = await app.head('/reviews', headers=headers)
#     count = response.headers.get('Total-Count')

#     assert int(count) == 2


# async def test_reviews_get(app, headers) -> None:
#     response = await app.get('/reviews', headers=headers)
#     content = await response.text()

#     assert response.status == 200

#     data_dict = loads(content)

#     assert len(data_dict) == 2
#     assert data_dict[0]['id'] == 'LMK123'


# async def test_reviews_put(app, headers) -> None:
#     review_data = dumps([{
#         "id": "006",
#         "description": "Reporte Vigilante",
#         "employeeId": "MRTY123",
#         "origin": 'monitor',
#         "siteId": "QWTP456",
#         "approved": True,
#         "timestamp": 1543437086
#     }])

#     response = await app.put('/reviews', data=review_data, headers=headers)

#     content = await response.text()
#     assert response.status == 201


# async def test_reviews_delete(app, headers) -> None:
#     response = await app.delete('/reviews/LMK123', headers=headers)
#     content = await response.text()
#     assert response.status == 204

#     response = await app.get('/reviews', headers=headers)
#     data_dict = loads(await response.text())

#     assert len(data_dict) == 1


# async def test_review_delete_body(app, headers) -> None:
#     ids = dumps(["LMK123"])
#     response = await app.delete(
#         '/reviews', data=ids, headers=headers)
#     content = await response.text()
#     assert response.status == 204

#     response = await app.get('/reviews', headers=headers)
#     data_dict = loads(await response.text())

#     assert len(data_dict) == 1


# # Activities


# async def test_activities_head(app, headers) -> None:
#     response = await app.head('/activities', headers=headers)
#     count = response.headers.get('Total-Count')

#     assert int(count) == 2


# async def test_activities_get(app, headers) -> None:
#     response = await app.get('/activities', headers=headers)
#     content = await response.text()

#     assert response.status == 200

#     data_dict = loads(content)

#     assert len(data_dict) == 2
#     assert data_dict[0]['id'] == 'LMK123'


# async def test_activities_put(app, headers) -> None:
#     review_data = dumps([{
#         "id": "007",
#         "name": "Report Special",
#         "description": "Report Special Employee",
#         "activityType": 'RSE',
#     }])

#     response = await app.put('/activities', data=review_data, headers=headers)

#     content = await response.text()
#     assert response.status == 201


# async def test_activities_delete(app, headers) -> None:
#     response = await app.delete('/activities/LMK123', headers=headers)
#     content = await response.text()
#     assert response.status == 204

#     response = await app.delete('/activities', headers=headers)
#     content = await response.text()

#     response = await app.get('/activities', headers=headers)
#     data_dict = loads(await response.text())

#     assert len(data_dict) == 1


# # Sites


# async def test_sites_head(app, headers) -> None:
#     response = await app.head('/sites', headers=headers)
#     count = response.headers.get('Total-Count')

#     assert int(count) == 2


# async def test_sites_get(app, headers) -> None:
#     response = await app.get('/sites', headers=headers)
#     content = await response.text()

#     assert response.status == 200

#     data_dict = loads(content)

#     assert len(data_dict) == 2
#     assert data_dict[0]['id'] == 'XYX123'


# # Traces

# async def test_traces_head(app, headers) -> None:
#     response = await app.head('/traces', headers=headers)
#     count = response.headers.get('Total-Count')

#     assert int(count) == 2


# async def test_traces_get(app, headers) -> None:
#     response = await app.get('/traces', headers=headers)
#     content = await response.text()

#     assert response.status == 200

#     data_dict = loads(content)

#     assert len(data_dict) == 2
#     assert data_dict[0]['id'] == '001'


# async def test_traces_put(app, headers) -> None:
#     trace_data = dumps([{
#         "id": "007",
#         "latitude": 4.5656,
#         "longitude": -72.3456,
#         "timestamp": 1543437086
#     }])

#     response = await app.put('/traces', data=trace_data, headers=headers)
#     content = await response.text()
#     assert response.status == 201


# # Filter

# async def test_get_request_filter(app, headers) -> None:
#     response = await app.get(
#         '/occurrences?filter=[["type", "=", "Emergency 2"]]',
#         headers=headers)
#     content = await response.text()
#     data_dict = loads(content)
#     assert len(data_dict) == 1


# async def test_get_request_filter(app, headers) -> None:
#     response = await app.get(
#         '/occurrences?filter=[["TYPE", "=", "Emergency 2"]]',
#         headers=headers)
#     content = await response.text()
#     data_dict = loads(content)
#     assert len(data_dict) == 1


# async def test_get_request_filter_bad_domain(app, headers) -> None:
#     response = await app.get(
#         '/occurrences?filter=["=", "Emergency 2"]',
#         headers=headers)
#     content = await response.text()
#     data_dict = loads(content)
#     assert len(data_dict) == 1


# async def test_bad_filter_get_route_filter(app, headers) -> None:
#     response = await app.get('/occurrences?filter=[[**BAD FILTER**]]',
#                              headers=headers)
#     content = await response.text()
#     data_dict = loads(content)
#     assert len(data_dict) == 5

# # middleware


# async def test_occurrences_get_unauthorized(app) -> None:
#     response = await app.get('/occurrences')
#     content = await response.text()

#     assert response.status == 401
#     data_dict = loads(content)
#     assert 'error' in data_dict
