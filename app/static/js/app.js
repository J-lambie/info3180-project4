var app=angular.module('Wishlist',['ngRoute']);
app.config(['$routeProvider',function ($routeProvider) {
  $routeProvider
    .when('/', {
      templateUrl: 'static/templates/home.html'
    })
    .when('/login', {
      templateUrl: 'static/templates/login.html',
      controller: 'LoginController'
    })
    .when('/logout', {
      controller: 'LogoutController'
    })
    .when('/register', {
      templateUrl: 'static/templates/register.html',
      controller: 'registerController'
    })
    .when('/wishlist', {
      template: '<h1>This is page one!</h1>'
    })
    .when('/add', {
      template: '<h1>This is page two!</h1>'
    })
    .otherwise({
      redirectTo: '/'
    });
}]);