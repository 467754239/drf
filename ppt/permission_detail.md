## DRF Permission

AllowAny
```
任何人都可以访问
```

IsAdminUser
```
除了user.is_staff是true以外得user都会被拒绝，也就是管理员们才会被应许访问。
```

IsAuthenticated
```
只有注册用户才能访问
```

IsAuthenticatedOrReadOnly
```
注册用户可以以任何方法访问，没有注册得用户只能以安全方法（GET,HEAD,OPTIONS）访问。
这是用于你希望你的api可以被任何用户read，但是只能被注册用户write.
```

DjangoMOdelPermissions
```
这和Django得标准模块django.contrib.auth相联系。这个permission只能被用于有.queryset属性的views.只有用户是注册用户并且有相关model的权限时才会有效。

- POST
用户必须拥有add权限

- PUT和PATCH
用户必须拥有change权限

- DELETE
用户必须拥有delete权限
支持个性化model permission，比如你定制一个view的GET访问权限。
使用个性化权限需要覆盖DjangoModelPermissions并且设置.perms_map属性。
如果你把这个属性用在没有queryset这个属性的model上并且使用了get_queryset()方法。我们建议你在你的view里标记一个sentinel queryset,以便于这个类可以确定所需的权限。
queryset = User.objects.none()
```

DjangoModelPermissionsOrAnonReadOnly
```
类似DjangoModelPermissions,但是允许非注册用户以只读方式访问api
```

DjangoObjectPermissions
```
与Django的object permissions framework（对模型每个对象的权限）相联系。使用这个权限您还需要添加支持对象级权限的权限后端，例如django-guardian。
类似于DjangoModelPermissions,这个permission作用于有.queryset或.get_queryset()的view。只有有相关的per-object权限和相关的model权限才可以使用。
个性化权限需要覆盖DjangoObjectPermissions并且设置.per_map属性.
```

注意
```
你希望你的view的GET,HEAD,OPTIONS使用对象级的访问权限控制，你可以考添加DjangoObjectPermissionsFilter类
```


