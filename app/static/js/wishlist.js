var app = angular.module('Wishlist',[]);



app.controller('LoginController',function($scope,$http){
    $http.post('/api/Users/login',data,config).then(function(response){
         var info=response.data;
         console.log(info)
        
        });
});


