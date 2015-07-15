<%@page import="java.util.Enumeration"%>
<%@page import="com.mydomain.model.User"%>
<%@ page isELIgnored="false"%>
<%@ taglib uri="http://www.springframework.org/tags/form" prefix="springForm"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
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
<springForm:errors path="user.name" cssClass="error" /><br>
Age: 
<springForm:select path="user.age" items="${ageList}" ></springForm:select>
<!--   <input type="text" name="age" value="${u.age}"></input> -->
<springForm:errors path="user.age" cssClass="error" /><br>
<input type="submit" value="Save"></input><br>
</form>

</body>
</html>