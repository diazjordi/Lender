from rest_framework import serializers
from lender_api.models import Borrower, Item, Transaction


class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = ('id', 'first_name', 'last_name',
                  'allowed_to_borrow', 'phone')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'title', 'item_type', 'checked_out')


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'checked_out_date',
                  'checked_out_by', 'checked_out_item')
