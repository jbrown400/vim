Vim�UnDo� Ɂ�d576���u9����-	��؄�����      I        url(r'^fundamentals/$', views.fundamentals, name='fundamentals'),   
         5       5   5   5    W"E�   " _�                             ����                                                                                                                                                                                                                                                                                                                                                             W��    �                       �                  �               5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             W��     �                       �             5�_�                       0    ����                                                                                                                                                                                                                                                                                                                                                             W��     �               A        url(r'^$', views.currentProject, name="currentProjects"),5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             W��    �      	          5�_�                       1    ����                                                                                                                                                                                                                                                                                                                                                             W�9     �         	      D        url(r'^$', views.finishedProjects, name="FinishedProjects"),5�_�                       :    ����                                                                                                                                                                                                                                                                                                                                                             W�=     �         	      D        url(r'^$', views.finishedProjects, name="finishedProjects"),5�_�                       7    ����                                                                                                                                                                                                                                                                                                                                                             W�@     �         	      A        url(r'^$', views.currentProject, name="CurrentProjects"),5�_�      	                 6    ����                                                                                                                                                                                                                                                                                                                                                             W�B     �         	      A        url(r'^$', views.currentProject, name="Currentprojects"),5�_�      
           	      0    ����                                                                                                                                                                                                                                                                                                                                                             W�D    �         	      B        url(r'^$', views.currentProject, name="Current_projects"),5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                             W��     �         	      B        url(r'^$', views.currentProject, name="current_projects"),5�_�   
                        ����                                                                                                                                                                                                                                                                                                                                                             W��     �         	      E        url(r'^$', views.finishedProjects, name="finished_projects"),5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             W��     �      	   	      6        url(r'^$', views.interests, name="interests"),5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             W��    �      	   	      @        url(r'^/intersts/$', views.interests, name="interests"),5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             W��     �         	      T        url(r'^/current_projects/$', views.currentProject, name="current_projects"),5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             W��     �         	      X        url(r'^/finished_projects/$', views.finishedProjects, name="finished_projects"),5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             W��    �      	   	      A        url(r'^/interests/$', views.interests, name="interests"),5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             W�Z    �         	      ,        url(r'^$', views.home, name="home"),5�_�                       0    ����                                                                                                                                                                                                                                                                                                                                                             W�h    �         	      3        url(r'^justin/$', views.home, name="home"),5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             W�m   	 �         	      5        url(r'^justin/$', views.home, name="justin"),5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             W�u    �         
              �         	    5�_�                           ����                                                                                                                                                                                                                                                                                                                               /          /          /    W��    �         
      0        url(r'^$', views.resume, name="resume"),5�_�                       8    ����                                                                                                                                                                                                                                                                                                                                                             W��     �         
      S        url(r'^current_projects/$', views.currentProject, name="current_projects"),5�_�                       7    ����                                                                                                                                                                                                                                                                                                                                                             W��    �      
                 �      
   
    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             W�    �                W        url(r'^finished_projects/$', views.finishedProjects, name="finished_projects"),5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             W�y    �         
       5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             W܇     �               app_name = showcase5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             W܉    �               app_name = showcase'5�_�                       +    ����                                                                                                                                                                                                                                                                                                                                                             W�>    �               .        url(r'^$', views.home, name="justin"),5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             W�     �      	         T        url(r'^current_projects/$', views.currentProjects, name="current_projects"),5�_�                       A    ����                                                                                                                                                                                                                                                                                                                                                             W�    �      	         L        url(r'^projects/$', views.currentProjects, name="current_projects"),5�_�                        *    ����                                                                                                                                                                                                                                                                                                                                                             W�    �      	         D        url(r'^projects/$', views.currentProjects, name="projects"),5�_�      !                  <    ����                                                                                                                                                                                                                                                                                                                                                             WJ�     �      
                 �      
       5�_�       "           !   	   -    ����                                                                                                                                                                                                                                                                                                                                                             WJ�     �      
         N        url(r'^projects/(?P<project_id>[0-9]+/$', views.detail, name='detail')5�_�   !   $           "   	   O    ����                                                                                                                                                                                                                                                                                                                                                             WJ�    �      
         O        url(r'^projects/(?P<project_id>[0-9]+)/$', views.detail, name='detail')5�_�   "   %   #       $   	   F    ����                                                                                                                                                                                                                                                                                                                                                             WSe     �      
         P        url(r'^projects/(?P<project_id>[0-9]+)/$', views.detail, name='detail'),5�_�   $   &           %   	   M    ����                                                                                                                                                                                                                                                                                                                                                             WSg    �      
         P        url(r'^projects/(?P<project_id>[0-9]+)/$', views.detail, name="detail'),5�_�   %   '           &      1    ����                                                                                                                                                                                                                                                                                                                                                             WSt     �      	         =        url(r'^projects/$', views.projects, name="projects"),5�_�   &   (           '      :    ����                                                                                                                                                                                                                                                                                                                                                             WSv    �      	         =        url(r'^projects/$', views.projects, name='projects"),5�_�   '   )           (   	   F    ����                                                                                                                                                                                                                                                                                                                                                             WS�     �      
         P        url(r'^projects/(?P<project_id>[0-9]+)/$', views.detail, name="detail"),5�_�   (   *           )   	   M    ����                                                                                                                                                                                                                                                                                                                                                             WS�     �      
         P        url(r'^projects/(?P<project_id>[0-9]+)/$', views.detail, name='detail"),5�_�   )   +           *   
   F    ����                                                                                                                                                                                                                                                                                                                                                             WS�     �   	            I        url(r'^fundamentals/$', views.fundamentals, name="fundamentals"),5�_�   *   ,           +   
   9    ����                                                                                                                                                                                                                                                                                                                                                             WS�     �   	            I        url(r'^fundamentals/$', views.fundamentals, name="fundamentals'),5�_�   +   -           ,      =    ����                                                                                                                                                                                                                                                                                                                                                             WS�     �   
            @        url(r'^interests/$', views.interests, name="interests"),5�_�   ,   .           -      3    ����                                                                                                                                                                                                                                                                                                                                                             WS�     �   
            @        url(r'^interests/$', views.interests, name="interests'),5�_�   -   /           .      4    ����                                                                                                                                                                                                                                                                                                                                                             WS�     �               7        url(r'^resume/$', views.resume, name="resume"),5�_�   .   0           /      -    ����                                                                                                                                                                                                                                                                                                                                                             WS�     �               7        url(r'^resume/$', views.resume, name="resume'),5�_�   /   1           0      )    ����                                                                                                                                                                                                                                                                                                                                                             WS�     �               ,        url(r'^$', views.home, name="home"),5�_�   0   3           1      $    ����                                                                                                                                                                                                                                                                                                                                                             WS�     �               ,        url(r'^$', views.home, name="home'),5�_�   1   4   2       3   
       ����                                                                                                                                                                                                                                                                                                                                                             W"E�     �   	            I        url(r'^fundamentals/$', views.fundamentals, name='fundamentals'),5�_�   3   5           4   
   B    ����                                                                                                                                                                                                                                                                                                                                                             W"E�   ! �   	            E        url(r'^concepts/$', views.fundamentals, name='fundamentals'),5�_�   4               5   
   .    ����                                                                                                                                                                                                                                                                                                                                                             W"E�   " �   	            A        url(r'^concepts/$', views.fundamentals, name='concepts'),5�_�   1           3   2          ����                                                                                                                                                                                                                                                                                                                                                             WT$    �      	         <        url(r'^projects/', views.projects, name='projects'),5�_�   "           $   #   	       ����                                                                                                                                                                                                                                                                                                                                                             WRq    �      
         G        url(r'^(?P<project_id>[0-9]+)/$', views.detail, name='detail'),5��