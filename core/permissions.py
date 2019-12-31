from rest_framework import serializers
from rest_framework import permissions
from .models import *


class ClientPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
   
        try: 
            try:

                if request.method == "GET" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif Client.objects.filter(email=request.user.email).exists():
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True
                
                elif request.method == "POST":
                    return True

                elif request.method == "PUT" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif Client.objects.filter(email=request.user.email).exists():
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "PATCH" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif Client.objects.filter(email=request.user.email).exists():
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "DELETE" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "OPTIONS":
                    return True

                elif request.method == "HEAD":
                    return True

            except Manager.DoesNotExist:
                return False
        except Client.DoesNotExist:
            return False


class AddressPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        try: 
            try:

                if request.method == "GET" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif Client.objects.filter(email=request.user.email).exists():
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True
                
                elif request.method == "POST":
                    return True

                elif request.method == "PUT" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif Client.objects.filter(email=request.user.email).exists():
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "PATCH" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif Client.objects.filter(email=request.user.email).exists():
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "DELETE" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "OPTIONS":
                    return True

                elif request.method == "HEAD":
                    return True

            except Manager.DoesNotExist:
                return False
        except Client.DoesNotExist:
            return False
        

class ManagerPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        try: 
            try:

                if request.method == "GET" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True
                
                elif request.method == "POST":
                    if request.user.is_superuser:
                        return True
                
                elif request.method == "PUT" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "PATCH" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "DELETE" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "OPTIONS":
                    return True

                elif request.method == "HEAD":
                    return True

            except Manager.DoesNotExist:
                return False
        except Client.DoesNotExist:
            return False


class BookPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
       
        try: 
            try:

                if request.method == "GET":
                    return True
                
                elif request.method == "POST" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True
                
                elif request.method == "PUT" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "PATCH" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "DELETE" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "OPTIONS":
                    return True

                elif request.method == "HEAD":
                    return True

            except Manager.DoesNotExist:
                return False
        except Client.DoesNotExist:
            return False


class StatusPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        try: 
            try:

                if request.method == "GET":
                    return True
                
                elif request.method == "POST" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "PUT" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "PATCH" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "DELETE" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "OPTIONS":
                    return True

                elif request.method == "HEAD":
                    return True

            except Manager.DoesNotExist:
                return False
        except Client.DoesNotExist:
            return False


class GenrerPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        try: 
            try:

                if request.method == "GET":
                    return True
                
                elif request.method == "POST" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "PUT" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "PATCH" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "DELETE" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "OPTIONS":
                    return True

                elif request.method == "HEAD":
                    return True

            except Manager.DoesNotExist:
                return False
        except Client.DoesNotExist:
            return False


class AuthorPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        try: 
            try:

                if request.method == "GET":
                    return True
                
                elif request.method == "POST" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "PUT" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "PATCH" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "DELETE" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "OPTIONS":
                    return True

                elif request.method == "HEAD":
                    return True

            except Manager.DoesNotExist:
                return False
        except Client.DoesNotExist:
            return False


class WritePermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        try: 
            try:

                if request.method == "GET":
                    return True
                
                elif request.method == "POST" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "PUT" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "PATCH" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "DELETE" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "OPTIONS":
                    return True

                elif request.method == "HEAD":
                    return True

            except Manager.DoesNotExist:
                return False
        except Client.DoesNotExist:
            return False
  

class OrderPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        try: 
            try:

                if request.method == "GET" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True
                    elif Client.objects.filter(email=request.user.email).exists():
                        return True

                elif request.method == "POST" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True
                    elif Client.objects.filter(email=request.user.email).exists():
                        return True

                elif request.method == "PUT" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "PATCH" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "DELETE" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "OPTIONS":
                    return True

                elif request.method == "HEAD":
                    return True

            except Manager.DoesNotExist:
                return False
        except Client.DoesNotExist:
            return False


class ItemOrderPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        try: 
            try:

                if request.method == "GET" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True
                    elif Client.objects.filter(email=request.user.email).exists():
                        return True

                elif request.method == "POST" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True
                    elif Client.objects.filter(email=request.user.email).exists():
                        return True

                elif request.method == "PUT" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "PATCH" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "DELETE" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "OPTIONS":
                    return True

                elif request.method == "HEAD":
                    return True

            except Manager.DoesNotExist:
                return False
        except Client.DoesNotExist:
            return False


class CreditCardPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        try: 
            try:

                if request.method == "GET" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True
                    elif Client.objects.filter(email=request.user.email).exists():
                        return True

                elif request.method == "POST" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True
                    elif Client.objects.filter(email=request.user.email).exists():
                        return True

                elif request.method == "PUT" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True
                    elif Client.objects.filter(email=request.user.email).exists():
                        return True

                elif request.method == "PATCH" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True
                    elif Client.objects.filter(email=request.user.email).exists():
                        return True

                elif request.method == "DELETE" and request.user.is_authenticated:
                    if request.user.is_superuser:
                        return True
                    elif (Manager.objects.get(email=request.user.email).user.is_staff):
                        return True

                elif request.method == "OPTIONS":
                    return True

                elif request.method == "HEAD":
                    return True

            except Manager.DoesNotExist:
                return False
        except Client.DoesNotExist:
            return False
