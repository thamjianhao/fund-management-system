from .models import Fund
from .serializers import FundSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def fund_list(request, format=None):
    """
    List all funds or create a new fund.

    **Request Methods:**

    `GET`
        Returns a list of all funds.

    `POST`
        Create a new fund instance.

    **Request Format (POST):**

    .. code-block:: json

        {
            "fund_id": "TECH001",
            "fund_name": "Technology Growth Fund",
            "fund_manager_name": "Jane Smith",
            "fund_description": "A fund focused on high-growth tech companies",
            "fund_nav": "1000000.00",
            "date_of_creation": "2024-01-01",
            "fund_performance": "15.50"
        }

    **Response Format:**

    `GET`
        Returns a list of all funds with status code 200 (OK).

    `POST` (Success)
        Returns the created fund data with status code 201 (Created).

    `POST` (Error)
        Returns validation errors with status code 400 (Bad Request).

    **Status Codes:**

    - 200 OK -- Request succeeded for GET
    - 201 Created -- Fund was successfully created
    - 400 Bad Request -- Validation failed
    """

    if request.method == 'GET':
        funds = Fund.objects.all()
        serializer = FundSerializer(funds, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = FundSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def fund_detail(request, id, format=None):
    """
    Retrieve, update or delete a fund instance.

    **URL Parameters:**

    ``id``
        The unique identifier of the :model:`funds.Fund` to operate on.

    **Request Methods:**

    `GET`
        Returns the specified fund.

    `PUT`
        Update the specified fund.

    `DELETE`
        Remove the specified fund.

    **Request Format (PUT):**

    .. code-block:: json

        {
            "fund_id": "TECH001",
            "fund_name": "Technology Growth Fund Updated",
            "fund_manager_name": "Jane Smith",
            "fund_description": "Updated description",
            "fund_nav": "1100000.00",
            "date_of_creation": "2024-01-01",
            "fund_performance": "16.50"
        }

    **Response Format:**

    `GET`
        Returns the fund data with status code 200 (OK).

    `PUT` (Success)
        Returns the updated fund data with status code 200 (OK).

    `PUT` (Error)
        Returns validation errors with status code 400 (Bad Request).

    `DELETE`
        Returns no content with status code 204 (No Content).

    **Status Codes:**

    - 200 OK -- Request succeeded for GET, PUT
    - 204 No Content -- Fund was successfully deleted
    - 400 Bad Request -- Validation failed
    - 404 Not Found -- Fund does not exist
    """

    try:
        fund = Fund.objects.get(pk=id)
    except Fund.DoesNotExist:
        return Response({"error": "Fund not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FundSerializer(fund)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = FundSerializer(fund, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        fund.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
