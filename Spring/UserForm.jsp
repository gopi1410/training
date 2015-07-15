<%@page import="com.mydomain.model.User"%>
<%@ page isELIgnored="false"%>
<%@ taglib uri="http://www.springframework.org/tags/form" prefix="springForm"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
<form action="addUser" method="post" name="user">
<input type="hidden" value="${user.id}" name="id"></input>
Name: <input type="text" name="name" value="${user.name}"></input>
<br>
Age:    <input type="text" name="age" value="${user.age}"></input>
<br>
<input type="submit" value="Save"></input><br>
</form>

</body>
</html>