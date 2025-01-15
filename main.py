from flask import Flask, request, jsonify

app = Flask(__name__)

#https://gwcloud.byappdirect.com/api/billing/v2/payments/paymentConnectors/capabilities
#https://gwcloud.byappdirect.com/api/billing/v2/payments/paymentConnectors

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
    print("Request Headers:", request.headers)
    print("Request JSON:", request.get_json())
    response =  jsonify({
    "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJTT3VBV0VZTjlOVGU4U3pXODRhcUp0U0ZzSVF3YWs2QmhndTJCd2JfaTZNIn0.eyJleHAiOjE3MzY1MTIyNjMsImlhdCI6MTczNjQyNTg2MywianRpIjoiZGUzYzU3NDctOGU0Ny00Y2I3LThjZDgtNzNhYjk2ODdmYWJhIiwiaXNzIjoiaHR0cHM6Ly9hdXRoLnRlbGVjYWxsLXBvYy5zbWFydHBsYWNlLmNsb3VkL3JlYWxtcy9tYXN0ZXIiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiOTRjMTE3MTQtNTM4YS00ZjE3LWE1YjEtMWM3Y2M3ODdjOWVkIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiYWRtaW4tdWkiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbImh0dHA6Ly9sb2NhbGhvc3Q6MzAwMCIsImh0dHBzOi8vYWRtaW4tdWkudGVsZWNhbGwtcG9jLnNtYXJ0cGxhY2UuY2xvdWQiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImRlZmF1bHQtcm9sZXMtbWFzdGVyIiwib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFkbWluLXVpIjp7InJvbGVzIjpbInVtYV9wcm90ZWN0aW9uIl19LCJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6InByb2ZpbGUgZW1haWwiLCJjbGllbnRIb3N0IjoiMTc5LjgzLjUuMTUwIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJzZXJ2aWNlLWFjY291bnQtYWRtaW4tdWkiLCJjbGllbnRBZGRyZXNzIjoiMTc5LjgzLjUuMTUwIiwiY2xpZW50X2lkIjoiYWRtaW4tdWkifQ.DjT2b1UabHAeyffm0irnqUaLWr5X0-VGolmlM-WMPwty7Jv3okV09Jb_C_CeBiC0uZtxdyAqkzB6VEovDTMD2WH3h6_wm1yA3UG_3Ht8q9cwG_Tdtgte24tpEhkGuJF645OLzJzuN0tiEw82rqokqEV0JMScNdw8LHSLL34N1kBr93xQMR-1w-PfdV85AS1BSBc7g1JDrh4QGmxZksj82d2cWaPq7LpclyB_S9UmSDxf6zI0x-ShJQFQvZ-CnQqfMlREoHwGV5P30E3zayPcIiuxYBEhJIbmYdbJQE7Txx7DtP9mIiNjhGzpKycaNVGDAeU9mTlwS3-qmwYcBNxmsA",
    "expires_in": 86400,
    "refresh_expires_in": 0,
    "token_type": "Bearer",
    "not-before-policy": 0,
    "scope": "profile email"})
    print("Response JSON:", response.get_json())
    return response

@app.route('/token', methods=['POST'])
def generate_token():
    print("/token++++++++++++++++++++++")
    print("Request Headers:", request.headers)
    print("Request JSON:", request.get_json())
    print("/token++++++++++++++++++++++")
    return jsonify({
    "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJTT3VBV0VZTjlOVGU4U3pXODRhcUp0U0ZzSVF3YWs2QmhndTJCd2JfaTZNIn0.eyJleHAiOjE3MzY1MTIyNjMsImlhdCI6MTczNjQyNTg2MywianRpIjoiZGUzYzU3NDctOGU0Ny00Y2I3LThjZDgtNzNhYjk2ODdmYWJhIiwiaXNzIjoiaHR0cHM6Ly9hdXRoLnRlbGVjYWxsLXBvYy5zbWFydHBsYWNlLmNsb3VkL3JlYWxtcy9tYXN0ZXIiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiOTRjMTE3MTQtNTM4YS00ZjE3LWE1YjEtMWM3Y2M3ODdjOWVkIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiYWRtaW4tdWkiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbImh0dHA6Ly9sb2NhbGhvc3Q6MzAwMCIsImh0dHBzOi8vYWRtaW4tdWkudGVsZWNhbGwtcG9jLnNtYXJ0cGxhY2UuY2xvdWQiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImRlZmF1bHQtcm9sZXMtbWFzdGVyIiwib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFkbWluLXVpIjp7InJvbGVzIjpbInVtYV9wcm90ZWN0aW9uIl19LCJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6InByb2ZpbGUgZW1haWwiLCJjbGllbnRIb3N0IjoiMTc5LjgzLjUuMTUwIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJzZXJ2aWNlLWFjY291bnQtYWRtaW4tdWkiLCJjbGllbnRBZGRyZXNzIjoiMTc5LjgzLjUuMTUwIiwiY2xpZW50X2lkIjoiYWRtaW4tdWkifQ.DjT2b1UabHAeyffm0irnqUaLWr5X0-VGolmlM-WMPwty7Jv3okV09Jb_C_CeBiC0uZtxdyAqkzB6VEovDTMD2WH3h6_wm1yA3UG_3Ht8q9cwG_Tdtgte24tpEhkGuJF645OLzJzuN0tiEw82rqokqEV0JMScNdw8LHSLL34N1kBr93xQMR-1w-PfdV85AS1BSBc7g1JDrh4QGmxZksj82d2cWaPq7LpclyB_S9UmSDxf6zI0x-ShJQFQvZ-CnQqfMlREoHwGV5P30E3zayPcIiuxYBEhJIbmYdbJQE7Txx7DtP9mIiNjhGzpKycaNVGDAeU9mTlwS3-qmwYcBNxmsA",
    "expires_in": 86400,
    "refresh_expires_in": 0,
    "token_type": "Bearer",
    "not-before-policy": 0,
    "scope": "profile email"
})
    
@app.route('/', methods=['POST'])
def home():
    print("Request Headers:", request.headers)
    print("Request JSON:", request.get_json())
    response =  jsonify({
    "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJTT3VBV0VZTjlOVGU4U3pXODRhcUp0U0ZzSVF3YWs2QmhndTJCd2JfaTZNIn0.eyJleHAiOjE3MzY1MTIyNjMsImlhdCI6MTczNjQyNTg2MywianRpIjoiZGUzYzU3NDctOGU0Ny00Y2I3LThjZDgtNzNhYjk2ODdmYWJhIiwiaXNzIjoiaHR0cHM6Ly9hdXRoLnRlbGVjYWxsLXBvYy5zbWFydHBsYWNlLmNsb3VkL3JlYWxtcy9tYXN0ZXIiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiOTRjMTE3MTQtNTM4YS00ZjE3LWE1YjEtMWM3Y2M3ODdjOWVkIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiYWRtaW4tdWkiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbImh0dHA6Ly9sb2NhbGhvc3Q6MzAwMCIsImh0dHBzOi8vYWRtaW4tdWkudGVsZWNhbGwtcG9jLnNtYXJ0cGxhY2UuY2xvdWQiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImRlZmF1bHQtcm9sZXMtbWFzdGVyIiwib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFkbWluLXVpIjp7InJvbGVzIjpbInVtYV9wcm90ZWN0aW9uIl19LCJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6InByb2ZpbGUgZW1haWwiLCJjbGllbnRIb3N0IjoiMTc5LjgzLjUuMTUwIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJzZXJ2aWNlLWFjY291bnQtYWRtaW4tdWkiLCJjbGllbnRBZGRyZXNzIjoiMTc5LjgzLjUuMTUwIiwiY2xpZW50X2lkIjoiYWRtaW4tdWkifQ.DjT2b1UabHAeyffm0irnqUaLWr5X0-VGolmlM-WMPwty7Jv3okV09Jb_C_CeBiC0uZtxdyAqkzB6VEovDTMD2WH3h6_wm1yA3UG_3Ht8q9cwG_Tdtgte24tpEhkGuJF645OLzJzuN0tiEw82rqokqEV0JMScNdw8LHSLL34N1kBr93xQMR-1w-PfdV85AS1BSBc7g1JDrh4QGmxZksj82d2cWaPq7LpclyB_S9UmSDxf6zI0x-ShJQFQvZ-CnQqfMlREoHwGV5P30E3zayPcIiuxYBEhJIbmYdbJQE7Txx7DtP9mIiNjhGzpKycaNVGDAeU9mTlwS3-qmwYcBNxmsA",
    "expires_in": 86400,
    "refresh_expires_in": 0,
    "token_type": "Bearer",
    "not-before-policy": 0,
    "scope": "profile email"})
    print("Response JSON:", response.get_json())
    return response

@app.route('/oauth2/config/gocardless/setup', methods=['POST'])
def home():
    print("Request Headers:", request.headers)
    print("Request JSON:", request.get_json())
    response =  jsonify({
    "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJTT3VBV0VZTjlOVGU4U3pXODRhcUp0U0ZzSVF3YWs2QmhndTJCd2JfaTZNIn0.eyJleHAiOjE3MzY1MTIyNjMsImlhdCI6MTczNjQyNTg2MywianRpIjoiZGUzYzU3NDctOGU0Ny00Y2I3LThjZDgtNzNhYjk2ODdmYWJhIiwiaXNzIjoiaHR0cHM6Ly9hdXRoLnRlbGVjYWxsLXBvYy5zbWFydHBsYWNlLmNsb3VkL3JlYWxtcy9tYXN0ZXIiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiOTRjMTE3MTQtNTM4YS00ZjE3LWE1YjEtMWM3Y2M3ODdjOWVkIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiYWRtaW4tdWkiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbImh0dHA6Ly9sb2NhbGhvc3Q6MzAwMCIsImh0dHBzOi8vYWRtaW4tdWkudGVsZWNhbGwtcG9jLnNtYXJ0cGxhY2UuY2xvdWQiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImRlZmF1bHQtcm9sZXMtbWFzdGVyIiwib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFkbWluLXVpIjp7InJvbGVzIjpbInVtYV9wcm90ZWN0aW9uIl19LCJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6InByb2ZpbGUgZW1haWwiLCJjbGllbnRIb3N0IjoiMTc5LjgzLjUuMTUwIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJzZXJ2aWNlLWFjY291bnQtYWRtaW4tdWkiLCJjbGllbnRBZGRyZXNzIjoiMTc5LjgzLjUuMTUwIiwiY2xpZW50X2lkIjoiYWRtaW4tdWkifQ.DjT2b1UabHAeyffm0irnqUaLWr5X0-VGolmlM-WMPwty7Jv3okV09Jb_C_CeBiC0uZtxdyAqkzB6VEovDTMD2WH3h6_wm1yA3UG_3Ht8q9cwG_Tdtgte24tpEhkGuJF645OLzJzuN0tiEw82rqokqEV0JMScNdw8LHSLL34N1kBr93xQMR-1w-PfdV85AS1BSBc7g1JDrh4QGmxZksj82d2cWaPq7LpclyB_S9UmSDxf6zI0x-ShJQFQvZ-CnQqfMlREoHwGV5P30E3zayPcIiuxYBEhJIbmYdbJQE7Txx7DtP9mIiNjhGzpKycaNVGDAeU9mTlwS3-qmwYcBNxmsA",
    "expires_in": 86400,
    "refresh_expires_in": 0,
    "token_type": "Bearer",
    "not-before-policy": 0,
    "scope": "profile email"})
    print("Response JSON:", response.get_json())
    return response
    
    
@app.route('/capabilities', methods=['POST'])
def capabilities():
    print("/capabilities++++++++++++++++++++++")
    print("Request Headers:", request.headers)
    print("Request JSON:", request)
    print("/capabilities++++++++++++++++++++++")
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
    print("/preAuthorizations++++++++++++++++++++++")
    print("Request Headers:", request.headers)
    print("Request JSON:", request)
    print("/preAuthorizations++++++++++++++++++++++")
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
    print("/preAuthorizationId++++++++++++++++++++++")
    print("Request Headers:", request.headers)
    print("Request JSON:", request)
    print("/preAuthorizationId++++++++++++++++++++++")
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
    
@app.route('/payments', methods=['POST'])
def payments():
    print("/payments++++++++++++++++++++++")
    print("Request Headers:", request.headers)
    print("Request JSON:", request)
    print("/payments++++++++++++++++++++++")
    return jsonify({
  "id": "paymentId",
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
  },
  "intents": [
    {
      "targetIdentifier": "7e80b37a-448c-468c-ab23-fc63793e3e92",
      "targetType": "INVOICE",
      "amountToPay": 10,
      "content": "{ \"id\": \"7e80b37a-448c-468c-ab23-fc63793e3e92\" \"invoiceNumber\": \"1111\" \"status\": \"UNPAID\" \"currency\": \"USD\" \"invoiceDate\": \"2019-01-27\" \"lines\": [ \"id\": \"invoiceLineId\" \"description\": \"elastic.io - Recurring Edition - Monthly Fee Period from 12/27/18 to 01/27/19\" \"quantity\": \"1.00\" \"unitPrice\": \"10.00\" \"total\": \"10.00\" \"period\": \"start\": \"2018-12-27\" \"end\": \"2019-01-27\" \"orderRef\": \"orderId\", \"id\": \"invoiceLineId2\" \"description\": \"product - Recurring Edition - Monthly Fee Period from 12/27/18 to 01/27/19\" \"quantity\": \"4.00\" \"unitPrice\": \"50.00\" \"total\": \"200.00\" \"period\": \"start\": \"2018-12-27\" \"end\": \"2019-01-27\" \"orderRef\": \"orderId2\" ] \"totalTax\": \"30.00\" \"total\": \"240.00\" }"
    }
  ]
})
    
@app.route('/tokenizeAndPay', methods=['POST'])
def tokenizeAndPay():
    print("/tokenizeAndPay++++++++++++++++++++++")
    print("Request Headers:", request.headers)
    print("Request JSON:", request)
    print("/tokenizeAndPay++++++++++++++++++++++")
    return jsonify({
  "transactionMode": "LIVE",
  "connectorInvocationContext": {
    "config": {
      "merchantParameters": {
        "merchantParam1": "value1"
      }
    },
    "tenant": "APPDIRECT",
    "merchantOfRecordId": "APPDIRECT",
    "merchantOfRecordType": "TENANT",
    "connectorId": "6a9267f3-6f37-4a33-863e-e1fe99fa1bf6"
  },
  "paymentRequest": {
    "id": "string",
    "amount": "string",
    "currency": "AOP",
    "intents": [
      {
        "targetIdentifier": "string",
        "targetType": "string",
        "amountToPay": "string",
        "content": "string"
      }
    ],
    "paymentProperties": {
      "additionalProp1": "string",
      "additionalProp2": "string",
      "additionalProp3": "string"
    }
  },
  "tokenizationRequest": {
    "paymentMethod": {
      "type": "CARD",
      "properties": {
        "number": "4111111111111111",
        "securityCode": "123",
        "cardHolderName": "Bob Dylan",
        "expirationMonth": "5",
        "expirationYear": "2019"
      },
      "status": "SUCCESS"
    }
  }
})

@app.route('/payments/<paymentId>', methods=['POST'])
def paymentId(paymentId):
    print("/paymentId++++++++++++++++++++++")
    print(paymentId)
    print("Request Headers:", request.headers)
    print("Request JSON:", request)
    print("/paymentId++++++++++++++++++++++")
    return jsonify({
  "PaymentMethod": {
    "type": "CARD",
    "token": "tokenId",
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
    
    
@app.route('/payments/initRedirect', methods=['POST'])
def initRedirect():
    print("/initRedirect++++++++++++++++++++++")
    print("Request Headers:", request.headers)
    print("Request JSON:", request)
    print("/initRedirect++++++++++++++++++++++")
    return jsonify({
  "invoiceNumber": "1232",
  "paymentMethodId": "3221",
  "partyType": "USER",
  "partyId": "da2bf844-5058-4a4d-bd57-0b1e82838f1f",
  "ownerUserId": "4db155c6-4459-46e3-984f-fdb3e4a1a2e6",
  "ownerCompanyId": "15b26f6b-f252-4b78-890b-942aaf9a9983",
  "userFlow": "BILLING_INFO",
  "isSessionImpersonated": False,
  "isChannelAssistedFlow": False,
  "isResellerAssistedFlow": False,
  "returnUrlSuccess": "https://success.com",
  "returnUrlFailure": "https://failure.com",
  "locale": "en-US",
  "amount": "1000.00",
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
    
@app.route('/payments/finalizeRedirect', methods=['POST'])
def finalizeRedirect():
    print("/finalizeRedirect++++++++++++++++++++++")
    print("Request Headers:", request.headers)
    print("Request JSON:", request)
    print("/finalizeRedirect++++++++++++++++++++++")
    return jsonify({
  "amount": "1000.00",
  "currency": "USD",
  "parameters": {
    "adPaymentUuid": "47d1ed9a-7e89-49f5-8724-b057a49abb8c"
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


@app.route('/refunds', methods=['POST'])
def refunds():
    print("/refunds++++++++++++++++++++++")
    print("Request Headers:", request.headers)
    print("Request JSON:", request)
    print("/refunds++++++++++++++++++++++")
    return jsonify({
  "id": "paymentId",
  "paymentId": "paymentId",
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
    "merchantOfRecordType": "TENANT",
    "metadata": {
      "orderCode": "12345"
    }
  }
})


@app.route('/refunds/<refundId>', methods=['POST'])
def refundId(refundId):
    print("/refundId++++++++++++++++++++++")
    print(refundId)
    print("Request Headers:", request.headers)
    print("Request JSON:", request)
    print("/refundId++++++++++++++++++++++")
    return jsonify({
  "PaymentMethod": {
    "type": "CARD",
    "token": "tokenId",
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


@app.route('/paymentMethods/import', methods=['POST'])
def paymentMethodsImport():
    print("/paymentMethodsImport++++++++++++++++++++++")
    print("Request Headers:", request.headers)
    print("Request JSON:", request)
    print("/paymentMethodsImport++++++++++++++++++++++")
    return jsonify({
  "paymentMethodType": "CARD",
  "companyUuid": "59bacce6-3807-4d1f-9a98-b82a09bdab60",
  "userUuid": "d7148330-d372-412a-b14c-81b92851af68",
  "token": "cbcfcd41-6029-49fe-88ab-7ee0803e401c",
  "locale": "de-DE",
  "properties": {
    "firstName": "Lorel",
    "lastName": "Ipsum",
    "vatID": 123,
    "invoiceEmail": "lorel.ipsum@appdirect.com"
  },
  "billingAddress": {
    "city": "Montreal",
    "companyName": "DT",
    "country": "DE",
    "street1": "Gendarmenmarkt",
    "zip": "10115",
    "salutation": "Company",
    "phone": "+4912345678",
    "region": "Berlin"
  },
  "connectorInvocationContext": {
    "config": {
      "merchantParameters": {
        "merchantParam1": "value1"
      }
    },
    "tenant": "APPDIRECT",
    "merchantOfRecordId": "APPDIRECT",
    "merchantOfRecordType": "TENANT",
    "connectorId": "6a9267f3-6f37-4a33-863e-e1fe99fa1bf6"
  }
})


@app.route('/paymentMethods/initRedirect', methods=['POST'])
def paymentMethodsInitRedirect():
    print("/paymentMethodsInitRedirect++++++++++++++++++++++")
    print("Request Headers:", request.headers)
    print("Request JSON:", request)
    print("/paymentMethodsInitRedirect++++++++++++++++++++++")
    return jsonify({
  "partyType": "USER",
  "partyId": "da2bf844-5058-4a4d-bd57-0b1e82838f1f",
  "ownerUserId": "4db155c6-4459-46e3-984f-fdb3e4a1a2e6",
  "ownerCompanyId": "15b26f6b-f252-4b78-890b-942aaf9a9983",
  "userFlow": "BILLING_INFO",
  "isSessionImpersonated": False,
  "isChannelAssistedFlow": False,
  "isResellerAssistedFlow": False,
  "paymentMethodType": "SNAP",
  "returnUrlSuccess": "https://success.com",
  "returnUrlFailure": "https://failure.com",
  "locale": "en-US",
  "connectorInvocationContext": {
    "config": {
      "merchantParameters": {
        "merchantParam1": "value1"
      }
    },
    "tenant": "APPDIRECT",
    "merchantOfRecordId": "APPDIRECT",
    "merchantOfRecordType": "TENANT"
  },
  "customAttributeProperties": {
    "USER": {
      "properties": {
        "userCustomAttribute1": "value1"
      }
    }
  }
})


@app.route('/paymentMethods/finalizeRedirect', methods=['POST'])
def paymentMethodsFinalizeRedirect():
    print("/paymentMethodsFinalizeRedirect++++++++++++++++++++++")
    print("Request Headers:", request.headers)
    print("Request JSON:", request)
    print("/paymentMethodsFinalizeRedirect++++++++++++++++++++++")
    return jsonify({
  "parameters": {
    "adPaymentMethodId": "47d1ed9a-7e89-49f5-8724-b057a49abb8c"
  },
  "connectorInvocationContext": {
    "config": {
      "merchantParameters": {
        "merchantParam1": "value1"
      }
    },
    "tenant": "APPDIRECT",
    "merchantOfRecordId": "APPDIRECT",
    "merchantOfRecordType": "TENANT",
    "companyUuid": "015c0cb6-ba73-45d9-bab1-4278a8513c10",
    "userUuid": "700fba30-0aab-4eae-b09a-1dc961ed6f11"
  }
})


@app.route('/notifications', methods=['POST'])
def notifications():
    print("/notifications++++++++++++++++++++++")
    print("Request Headers:", request.headers)
    print("Request JSON:", request)
    print("/notifications++++++++++++++++++++++")
    return jsonify({
  "gatewayQueryParams": {
    "referenceNumber": "1022778335"
  },
  "gatewayPayload": "payload",
  "gatewayHeaders": {
    "Webhook-Signature": [
      "HMAC-SHA1"
    ]
  },
  "tenant": "APPDIRECT"
})



    
    
    
if __name__ == '__main__':
    app.run(debug=True)
