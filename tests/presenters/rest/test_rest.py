# from json import loads, dumps
# from instark.presenters.rest import RestApplication
# from instark.presenters.rest import rest as rest_module


# async def test_rest_application_run(monkeypatch):
#     called = False

#     class web:
#         @staticmethod
#         async def _run_app(app, port=1234):
#             nonlocal called
#             called = True

#     monkeypatch.setattr(rest_module, 'web', web)

#     await RestApplication.run(None)

#     assert called is True


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


# # Occurrence


# async def test_occurrences_head(app, headers) -> None:
#     response = await app.head('/occurrences', headers=headers)
#     count = response.headers.get('Total-Count')

#     assert int(count) == 5


# async def test_occurrences_get_unauthorized(app) -> None:
#     response = await app.get('/occurrences')
#     content = await response.text()

#     assert response.status == 401
#     data_dict = loads(content)
#     assert 'error' in data_dict


# async def test_occurrences_get(app, headers) -> None:
#     response = await app.get('/occurrences', headers=headers)
#     content = await response.text()
#     assert response.status == 200

#     data_dict = loads(content)

#     assert len(data_dict) == 5
#     assert data_dict[0]['id'] == 'ABC123'


# async def test_occurrences_get_route_filter(app, headers) -> None:
#     response = await app.get(
#         '/occurrences?filter=[["type", "=", "Emergency"]]',
#         headers=headers)
#     content = await response.text()
#     data_dict = loads(content)
#     assert len(data_dict) == 1


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
#     assert response.status == 200


# async def test_bad_filter_get_route_filter(app, headers) -> None:
#     response = await app.get('/occurrences?filter=[[**BAD FILTER**]]',
#                              headers=headers)
#     content = await response.text()
#     data_dict = loads(content)
#     assert len(data_dict) == 5


# async def test_occurrences_not_implemented_delete(app, headers) -> None:
#     response = await app.delete('/occurrences/ABC123', headers=headers)
#     content = await response.text()
#     assert response.status == 500


# # Activities


# async def test_activities_put(app, headers) -> None:
#     review_data = dumps([{
#         "id": "007",
#         "name": "Report Special",
#         "description": "Report Special Employee",
#         "activityType": 'RSE',
#     }])

#     response = await app.put('/activities', data=review_data, headers=headers)

#     content = await response.text()
#     assert response.status == 200


# async def test_activities_delete(app, headers) -> None:
#     response = await app.delete('/activities/LMK123', headers=headers)
#     content = await response.text()
#     assert response.status == 204

#     response = await app.delete('/activities', headers=headers)
#     content = await response.text()

#     response = await app.get('/activities', headers=headers)
#     data_dict = loads(await response.text())

#     assert len(data_dict) == 1


# # async def test_occurrences_delete(app, headers) -> None:
#     # response = await app.delete('/occurrences/LMK123', headers=headers)
#     # content = await response.text()
#     # assert response.status == 204

#     # response = await app.get('/occurrences', headers=headers)
#     # data_dict = loads(await response.text())

#     # assert len(data_dict) == 2


# async def test_activities_delete_body(app, headers) -> None:
#     ids = dumps(["LMK123"])
#     response = await app.delete(
#         '/activities', data=ids, headers=headers)
#     content = await response.text()
#     assert response.status == 204

#     response = await app.get('/activities', headers=headers)
#     data_dict = loads(await response.text())

#     assert len(data_dict) == 1


# async def test_activities_get_route_filter(app, headers) -> None:
#     response = await app.get(
#         '/activities?filter=[["activityType", "=", "EMG"]]',
#         headers=headers)
#     content = await response.text()
#     data_dict = loads(content)
#     assert len(data_dict) == 1

# # async def test_questions_get(app, headers) -> None:
#     # response = await app.get('/questions', headers=headers)
#     # content = await response.text()

#     # assert response.status == 200

#     # data_dict = loads(content)

#     # assert len(data_dict) == 1
#     # assert data_dict[0]['id'] == '001'


# # async def test_questions_get_route_filter(app, headers) -> None:
#     # response = await app.get(
#     # '/questions?filter=[["occurrenceId", "=", "LMK123"]]',
#     # headers=headers)
#     # content = await response.text()
#     # data_dict = loads(content)
#     # assert len(data_dict) == 1


# # async def test_questions_head(app, headers) -> None:
#     # response = await app.head('/questions', headers=headers)
#     # count = response.headers.get('Total-Count')

#     # assert int(count) == 1


# # async def test_options_get(app, headers) -> None:
#     # response = await app.get('/options', headers=headers)
#     # content = await response.text()

#     # assert response.status == 200

#     # data_dict = loads(content)

#     # assert len(data_dict) == 1
#     # assert data_dict[0]['id'] == 'ABC'


# # async def test_options_head(app, headers) -> None:
#     # response = await app.head('/options', headers=headers)
#     # count = response.headers.get('Total-Count')

#     # assert int(count) == 1


# # async def test_assessments_head(app, headers) -> None:
#     # response = await app.head('/assessments', headers=headers)
#     # count = response.headers.get('Total-Count')

#     # assert int(count) == 2


# # async def test_assessments_get(app, headers) -> None:
#     # response = await app.get('/assessments', headers=headers)
#     # content = await response.text()

#     # assert response.status == 200

#     # data_dict = loads(content)

#     # assert len(data_dict) == 2
#     # assert data_dict[0]['id'] == '001'


# # async def test_assessments_put(app, headers) -> None:
#     # assessment_data = dumps([{
#     # 'id': '07506ce5-edd7-4eab-af9c-4e555bc8e098',
#     # 'occurrenceId': '07506ce5-edd7-4eab-af9c-4e555bc8e098',
#     # 'answers': [
#     # {
#     # 'value': 'Answer for second question',
#     # 'questionId': '635550e2-280f-4a84-9f93-992c2a7e4ba6'
#     # },
#     # {
#     # 'questionId': '9cec33fc-95c7-49fe-b35d-266cb578b778',
#     # 'optionIds': [
#     # "5ffcc875-7bc4-463d-b0bf-c34906857624",
#     # "b9ac29ae-0329-44e9-8435-34cce3aef58c"
#     # ]
#     # },
#     # ]}])

#     # response = await app.put('/assessments', data=assessment_data,
#     # headers=headers)
#     # content = await response.text()
#     # assert response.status == 200

#     # response = await app.head('/selections', headers=headers)
#     # count = response.headers.get('Total-Count')

#     # assert int(count) == 2

#     # response = await app.get('/selections', headers=headers)
#     # content = await response.text()

#     # assert response.status == 200

#     # data_dict = loads(content)

#     # assert len(data_dict) == 2


# # async def test_answers_head(app, headers) -> None:
#     # response = await app.head('/answers', headers=headers)
#     # count = response.headers.get('Total-Count')

#     # assert int(count) == 1


# # async def test_answers_get(app, headers) -> None:
#     # response = await app.get('/answers', headers=headers)
#     # content = await response.text()

#     # assert response.status == 200

#     # data_dict = loads(content)

#     # assert len(data_dict) == 1
#     # assert data_dict[0]['id'] == '001'


# # async def test_reports_count_answers_per_option(
#     # app, headers) -> None:
#     # response = await app.get(
#     # '/reports/count_answers_per_option?occurrenceId=001',
#     # headers=headers)
#     # content = await response.text()
#     # assert response.status == 200

#     # data_dict = loads(content)

#     # assert isinstance(data_dict, dict)
#     # assert 'fields' in data_dict
#     # assert 'rows' in data_dict
