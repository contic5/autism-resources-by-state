import get_excel_data from '/src/get_excel_data.js';

async function getText(file) {
  let myObject = await fetch(file);
  let myText = await myObject.text();
  myText=myText.replace(/(?:\r\n|\r|\n)/g, '<br>');
  console.log(`${file} ${myText}`);
  return myText;
}
function add_unique_states()
{
  let unique_states=[];
  for(let resource of resources)
  {
    unique_states.push(resource.State);
  }
  unique_states=new Set(unique_states);
  unique_states=[...unique_states];
  console.log(unique_states);

  for(let unique_state of unique_states)
  {
    let option=document.createElement("option");
    option.value=unique_state;
    option.innerHTML=unique_state;

    document.getElementById("states").appendChild(option);
  }
}
function write_resources(target_state)
{
  let filtered_resources=[...resources];
  filtered_resources=filtered_resources.filter(resource=>resource.State==target_state);
  console.log(filtered_resources);
  let bold_p=document.createElement("p");
  res.appendChild(bold_p);
  bold_p.style.fontWeight="bold";
  bold_p.innerHTML=`${target_state} Resources`;

  let ul=document.createElement("ul");
  res.appendChild(ul);
  for(let filtered_resource of filtered_resources)
  {
    let li=document.createElement("li");
    res.appendChild(li);
    li.innerHTML=filtered_resource.Resource+": ";

    let a=document.createElement("a");
    li.appendChild(a);
    a.href=filtered_resource.Link;
    a.innerHTML=filtered_resource.Link;
  }
}
function write_email()
{
  res.innerHTML="";
  let intro_p=document.createElement("p");
  res.appendChild(intro_p);
  intro_p.innerHTML=intro;
  if(email_app=="Wix")
  {
    intro_p+="<br>";
  }

  write_resources("National");
  if(state!="")
  {
    write_resources(state);
  }

  if(email_app=="Wix")
  {
    intro_p+="<br>";
  }

  let outro_p=document.createElement("p");
  res.appendChild(outro_p);
  outro_p.innerHTML=outro;
}
export function update_values()
{
  email_app=document.getElementById("email_app").value;
  state=document.getElementById("state_input").value;
  console.log(`State ${state}`);
  write_email();
}
function setup()
{
  add_unique_states();
  
}

let email_app=document.getElementById("email_app").value;
let state=document.getElementById("state_input").value;
const intro=await getText('/intro.txt');
const outro=await getText('/outro.txt');
const resources=await(get_excel_data("Autism Resources by State.xlsx"));
let res=document.getElementById("res");
setup();
write_email();