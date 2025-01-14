from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/tokens', methods=['POST'])
def tokens():
    return jsonify({
  "transactionMode": "LIVE",
  "paymentMethod": {
    "type": "CARD",
    "properties": {
      "number": "4111111111111111",
      "securityCode": "123",
      "cardHolderName": "Bob Dylan",
      "expirationMonth": "5",
      "expirationYear": "2019"
    }
  },
  "connectorInvocationContext": {
    "config": {
      "merchantParameters": {
        "merchantParam1": "value1"
      }
    },
    "tenant": "APPDIRECT",
    "merchantOfRecordId": "APPDIRECT",
    "merchantOfRecordType": "TENANT"
  }
})

@app.route('/paymentConnectors', methods=['POST'])
def paymentConnectors():
    return jsonify({
    "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJTT3VBV0VZTjlOVGU4U3pXODRhcUp0U0ZzSVF3YWs2QmhndTJCd2JfaTZNIn0.eyJleHAiOjE3MzY1MTIyNjMsImlhdCI6MTczNjQyNTg2MywianRpIjoiZGUzYzU3NDctOGU0Ny00Y2I3LThjZDgtNzNhYjk2ODdmYWJhIiwiaXNzIjoiaHR0cHM6Ly9hdXRoLnRlbGVjYWxsLXBvYy5zbWFydHBsYWNlLmNsb3VkL3JlYWxtcy9tYXN0ZXIiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiOTRjMTE3MTQtNTM4YS00ZjE3LWE1YjEtMWM3Y2M3ODdjOWVkIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiYWRtaW4tdWkiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbImh0dHA6Ly9sb2NhbGhvc3Q6MzAwMCIsImh0dHBzOi8vYWRtaW4tdWkudGVsZWNhbGwtcG9jLnNtYXJ0cGxhY2UuY2xvdWQiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImRlZmF1bHQtcm9sZXMtbWFzdGVyIiwib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFkbWluLXVpIjp7InJvbGVzIjpbInVtYV9wcm90ZWN0aW9uIl19LCJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6InByb2ZpbGUgZW1haWwiLCJjbGllbnRIb3N0IjoiMTc5LjgzLjUuMTUwIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJzZXJ2aWNlLWFjY291bnQtYWRtaW4tdWkiLCJjbGllbnRBZGRyZXNzIjoiMTc5LjgzLjUuMTUwIiwiY2xpZW50X2lkIjoiYWRtaW4tdWkifQ.DjT2b1UabHAeyffm0irnqUaLWr5X0-VGolmlM-WMPwty7Jv3okV09Jb_C_CeBiC0uZtxdyAqkzB6VEovDTMD2WH3h6_wm1yA3UG_3Ht8q9cwG_Tdtgte24tpEhkGuJF645OLzJzuN0tiEw82rqokqEV0JMScNdw8LHSLL34N1kBr93xQMR-1w-PfdV85AS1BSBc7g1JDrh4QGmxZksj82d2cWaPq7LpclyB_S9UmSDxf6zI0x-ShJQFQvZ-CnQqfMlREoHwGV5P30E3zayPcIiuxYBEhJIbmYdbJQE7Txx7DtP9mIiNjhGzpKycaNVGDAeU9mTlwS3-qmwYcBNxmsA",
    "expires_in": 86400,
    "refresh_expires_in": 0,
    "token_type": "Bearer",
    "not-before-policy": 0,
    "scope": "profile email"
})

@app.route('/token', methods=['POST'])
def generate_token():
    return jsonify({
    "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJTT3VBV0VZTjlOVGU4U3pXODRhcUp0U0ZzSVF3YWs2QmhndTJCd2JfaTZNIn0.eyJleHAiOjE3MzY1MTIyNjMsImlhdCI6MTczNjQyNTg2MywianRpIjoiZGUzYzU3NDctOGU0Ny00Y2I3LThjZDgtNzNhYjk2ODdmYWJhIiwiaXNzIjoiaHR0cHM6Ly9hdXRoLnRlbGVjYWxsLXBvYy5zbWFydHBsYWNlLmNsb3VkL3JlYWxtcy9tYXN0ZXIiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiOTRjMTE3MTQtNTM4YS00ZjE3LWE1YjEtMWM3Y2M3ODdjOWVkIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiYWRtaW4tdWkiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbImh0dHA6Ly9sb2NhbGhvc3Q6MzAwMCIsImh0dHBzOi8vYWRtaW4tdWkudGVsZWNhbGwtcG9jLnNtYXJ0cGxhY2UuY2xvdWQiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImRlZmF1bHQtcm9sZXMtbWFzdGVyIiwib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFkbWluLXVpIjp7InJvbGVzIjpbInVtYV9wcm90ZWN0aW9uIl19LCJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6InByb2ZpbGUgZW1haWwiLCJjbGllbnRIb3N0IjoiMTc5LjgzLjUuMTUwIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJzZXJ2aWNlLWFjY291bnQtYWRtaW4tdWkiLCJjbGllbnRBZGRyZXNzIjoiMTc5LjgzLjUuMTUwIiwiY2xpZW50X2lkIjoiYWRtaW4tdWkifQ.DjT2b1UabHAeyffm0irnqUaLWr5X0-VGolmlM-WMPwty7Jv3okV09Jb_C_CeBiC0uZtxdyAqkzB6VEovDTMD2WH3h6_wm1yA3UG_3Ht8q9cwG_Tdtgte24tpEhkGuJF645OLzJzuN0tiEw82rqokqEV0JMScNdw8LHSLL34N1kBr93xQMR-1w-PfdV85AS1BSBc7g1JDrh4QGmxZksj82d2cWaPq7LpclyB_S9UmSDxf6zI0x-ShJQFQvZ-CnQqfMlREoHwGV5P30E3zayPcIiuxYBEhJIbmYdbJQE7Txx7DtP9mIiNjhGzpKycaNVGDAeU9mTlwS3-qmwYcBNxmsA",
    "expires_in": 86400,
    "refresh_expires_in": 0,
    "token_type": "Bearer",
    "not-before-policy": 0,
    "scope": "profile email"
})
    
@app.route('/capabilities', methods=['POST'])
def capabilities():
    return jsonify(
  {
  "localizationIdentifier": "CONNECTOR_CYBERSOURCE",
  "connectPath": "/oauth2/config/gocardless/setup",
  "merchantAccountPropertiesDefinitions": [
    {
      "keyName": "consumerKey",
      "description": "The consumer key of the merchant account",
      "sensitive": False,
      "required": True
    },
    {
      "keyName": "consumerSecret",
      "description": "The consumer secret of the merchant account",
      "sensitive": True,
      "required": True
    }
  ],
  "merchantAccountParametersDefinitions": [
    {
      "name": "consumerKey",
      "type": "string",
      "sensitive": False,
      "required": True
    },
    {
      "name": "consumerSecret",
      "type": "string",
      "sensitive": True,
      "required": True
    }
  ],
  "paymentMethodDefinitions": [
    {
      "type": "CARD",
      "propertyDefinitions": [
        {
          "name": "cardHolderName",
          "type": "string",
          "minLength": 1,
          "maxLength": 255
        },
        {
          "name": "number",
          "type": "string",
          "minLength": 1,
          "maxLength": 50
        },
        {
          "name": "securityCode",
          "type": "string",
          "minLength": 1,
          "maxLength": 40,
          "secret": True
        },
        {
          "name": "expirationMonth",
          "type": "integer",
          "minLength": 1,
          "maxLength": 2
        },
        {
          "name": "expirationYear",
          "type": "integer",
          "minLength": 2,
          "maxLength": 4
        },
        {
          "name": "brand",
          "type": "string",
          "readOnly": True,
          "minLength": 1,
          "maxLength": 255
        }
      ],
      "supportedOperations": [
        "PREAUTHORIZATION",
        "PREAUTHORIZATION_PARTIAL_CAPTURE",
        "DIRECT_SALE",
        "REFUND",
        "PARTIAL_REFUND"
      ]
    },
    {
      "type": "ACH",
      "propertyDefinitions": [
        {
          "name": "institution",
          "type": "string",
          "minLength": 1,
          "maxLength": 255
        },
        {
          "name": "transit",
          "type": "string",
          "minLength": 1,
          "maxLength": 255
        }
      ],
      "supportedOperations": [
        "PREAUTHORIZATION",
        "PREAUTHORIZATION_PARTIAL_CAPTURE",
        "DIRECT_SALE",
        "REFUND",
        "PARTIAL_REFUND"
      ]
    }
  ],
  "invoiceDetailLevel": "SUMMARY"
}
)
    
@app.route('/preAuthorizations', methods=['POST'])
def preAuthorizations():
    return jsonify({
  "id": "ca4f9e54-8af9-11ea-bc55-0242ac130003",
  "paymentMethodToken": "d290f1ee-6c54-4b01-90e6-d701748f0851",
  "amount": "1000.00",
  "currency": "USD",
  "connectorInvocationContext": {
    "config": {
      "merchantParameters": {
        "merchantParam1": "value1"
      }
    },
    "tenant": "APPDIRECT",
    "merchantOfRecordId": "APPDIRECT",
    "merchantOfRecordType": "TENANT"
  }
})
    
@app.route('/preAuthorizations/<preAuthorizationId>', methods=['POST'])
def preAuthorizationId(preAuthorizationId):
    return jsonify({
  "connectorInvocationContext": {
    "config": {
      "merchantParameters": {
        "merchantParam1": "value1"
      }
    },
    "tenant": "APPDIRECT",
    "merchantOfRecordId": "APPDIRECT",
    "merchantOfRecordType": "TENANT"
  }
})


    
    
    
if __name__ == '__main__':
    app.run(debug=True)
