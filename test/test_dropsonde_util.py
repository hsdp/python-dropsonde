import six
import json
from unittest import TestCase
from base64 import b64decode, b64encode
from dropsonde import util
from google.protobuf import json_format
from dropsonde.pb.envelope_pb2 import Envelope


msg = """Cghnb3JvdXRlchAEMNGRj/XHrPSWFTq1Agil+t7zx6z0lhUQ1piO9ces9JYVGhUIjuT/mciS9aKsARDPvNWAwtCxjzIgASgBMiBodHRwOi8vbG9jYWxob3N0OjUwMDAvcm9ib3RzLnR4dDoOMTI3LjAuMC4xOjI0MDBCigFNb3ppbGxhLzUuMCAoTWFjaW50b3NoOyBJbnRlbCBNYWMgT1MgWCAxMF8xM180KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNjUuMC4zMzI1LjE4MSBTYWZhcmkvNTM3LjM2IE9QUi81Mi4wLjI4NzEuNjRIlANQ6QFiFAjr1LD9xZXrpBMQrc2W56WM5OFeaAByHDliODIyMjdiLWNmMDQtNGVhZi00ZTIwLWQzZjV6CTEyNy4wLjAuMWoHZXhhbXBsZXIGcm91dGVyeiRkNmI5MjFmMS0zMzBjLTQ0YjgtOWZkOS1jNWZmMWZmZDVlZDiCAQkxMjcuMC4wLjGKARUKCXNvdXJjZV9pZBIIZ29yb3V0ZXI="""


class Util(TestCase):
    def setUp(self):
        self.msg = b64decode(msg)

    def get_msg_json(self):
        env = Envelope()
        env.ParseFromString(self.msg)
        return json_format.MessageToJson(env)

    def test_parse_from_string(self):
        expected = {
            'origin': 'gorouter',
            'eventType': 'HttpStartStop',
            'timestamp': '1526106078300063953',
            'httpStartStop': {
              'startTimestamp': '1526106078297177381',
              'stopTimestamp': '1526106078300048470',
              'requestId': {
                'low': '12413561682238894606',
                'high': '3611542221973970511'
              },
              'peerType': 'Client',
              'method': 'GET',
              'uri': 'http://localhost:5000/robots.txt',
              'remoteAddress': '127.0.0.1:2400',
              'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36 OPR/52.0.2871.64',
              'statusCode': 404,
              'contentLength': '233',
              'applicationId': {
                'low': '1389831816359979627',
                'high': '6828460212163552941'
              },
              'instanceIndex': 0,
              'instanceId': '9b82227b-cf04-4eaf-4e20-d3f5',
              'forwarded': [
                '127.0.0.1'
              ]
            },
            'deployment': 'example',
            'job': 'router',
            'index': 'd6b921f1-330c-44b8-9fd9-c5ff1ffd5ed8',
            'ip': '127.0.0.1',
            'tags': {
              'source_id': 'gorouter'
            }
        }
        data = self.get_msg_json()
        self.assertDictEqual(json.loads(data), expected)

    def test_get_uuid_string(self):
        env = Envelope()
        env.ParseFromString(self.msg)
        data = json_format.MessageToJson(env)
        data = json.loads(data)

        app_uuid = data['httpStartStop']['applicationId']
        uuid = util.get_uuid_string(**app_uuid)
        self.assertEqual(uuid, '6b2aac5f-acac-4913-ada6-e55c6290c35e')

        uuid1 = {'low': 16232998280323427187, 'high': 16530230841049344141}
        uuid2 = util.get_uuid_string(**uuid1)
        self.assertEqual(uuid2, '736b340a-ee31-47e1-8de8-f3775e2d67e5')

        uuid1 = {'low': 5856609223220647014, 'high': 6860906074357131170}
        uuid2 = util.get_uuid_string(**uuid1)
        self.assertEqual(uuid2, '66d45712-0fdb-4651-a267-6057b9d5365f')

    def test_get_uuid_parts(self):
        parts = util.get_uuid_parts('66d45712-0fdb-4651-a267-6057b9d5365f')
        self.assertDictEqual(
            parts, {'low': 5856609223220647014, 'high': 6860906074357131170})

        parts = util.get_uuid_parts('736b340a-ee31-47e1-8de8-f3775e2d67e5')
        self.assertEqual(
            parts, {'low': 16232998280323427187, 'high': 16530230841049344141})

    def test_parse_part(self):
        encoded = util.parse_part(5856609223220647014)
        self.assertEqual(encoded, '66d457120fdb4651')

    def test_unparse_part(self):
        decoded = util.unparse_part('66d457120fdb4651')
        self.assertEqual(decoded, 5856609223220647014)
