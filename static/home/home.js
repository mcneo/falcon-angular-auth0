angular.module('base.home', [
    'auth0'
])
    .controller('HomeCtrl', function HomeController(
        $scope, auth, $http, $location, store
    ) {

        $scope.auth = auth;
        $scope.logs = {};

        $scope.logout = function () {
            auth.signout();
            store.remove('profile');
            store.remove('token');
            $location.path('/login');
        }

    });
