var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => "Hello ZODIACs!!!");

app.MapGet("/secret", (string? password) => 
{
  if (password == "secret123"){
    return "Nice you are our agent";
  }
  else {
    return "Access denied";
  }
});

app.Run();
