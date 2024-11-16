var display = document.getElementById('display');
function btnClick(value)
{
    display.value += value;
}

function clearDisplay()
{
    display.value="";
}

function result()
    {
      var res=eval(display.value)
      display.value=res;
    }
