# Copyright (C) 2010-2012 Yaco Sistemas (http://www.yaco.es)
# Copyright (C) 2009 Lorenzo Gil Sanchez <lorenzo.gil.sanchez@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#            http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.LoginView.as_view()),
    path("acs/", views.AssertionConsumerServiceView.as_view()),
    path("logout/", views.LogoutInitView.as_view()),
    path("ls/", views.LogoutView.as_view()),
    path("ls/post/", views.LogoutView.as_view()),
    path("metadata/", views.MetadataView.as_view()),
    path("login", views.LoginView.as_view(), name="saml2_login"),
    path("acs", views.AssertionConsumerServiceView.as_view(), name="saml2_acs"),
    path("logout", views.LogoutInitView.as_view(), name="saml2_logout"),
    path("ls", views.LogoutView.as_view(), name="saml2_ls"),
    path("ls/post", views.LogoutView.as_view(), name="saml2_ls_post"),
    path("metadata", views.MetadataView.as_view(), name="saml2_metadata"),
]
