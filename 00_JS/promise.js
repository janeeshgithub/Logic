const API_URL = "https://api.github.co/users/bye";
async function hp() {
  const d = await fetch(API_URL);
  const jv = await d.json();
  console.log(jv);
}
hp().catch((err) => console.error("err"));
hp();
