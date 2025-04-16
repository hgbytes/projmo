const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
canvas.width = window.innerWidth - 40;
canvas.height = window.innerHeight - 250;

let angleSlider = document.getElementById("angle");
let velocitySlider = document.getElementById("velocity");
let gravitySlider = document.getElementById("gravity");

let angle = parseFloat(angleSlider.value);
let velocity = parseFloat(velocitySlider.value);
let gravity = parseFloat(gravitySlider.value);

let time = 0;
let trajectory = [];

function reset() {
  angle = parseFloat(angleSlider.value);
  velocity = parseFloat(velocitySlider.value);
  gravity = parseFloat(gravitySlider.value);
  time = 0;
  trajectory = [];
}

angleSlider.oninput = () => {
  document.getElementById("angleVal").textContent = angleSlider.value;
  reset();
};

velocitySlider.oninput = () => {
  document.getElementById("velVal").textContent = velocitySlider.value;
  reset();
};

gravitySlider.oninput = () => {
  document.getElementById("gravVal").textContent = gravitySlider.value;
  reset();
};

function draw() {
  ctx.fillStyle = "#111";
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  const angleRad = (angle * Math.PI) / 180;
  const vx = velocity * Math.cos(angleRad);
  const vy = velocity * Math.sin(angleRad);
  const t = time;
  const x = vx * t;
  const y = vy * t - 0.5 * gravity * t * t;

  const posX = x;
  const posY = canvas.height - y;

  if (posY < canvas.height) {
    trajectory.push({ x: posX, y: posY });
  }

  for (let i = 0; i < trajectory.length; i++) {
    let hue = i * 2 % 360;
    ctx.fillStyle = `hsl(${hue}, 100%, 60%)`;
    ctx.beginPath();
    ctx.arc(trajectory[i].x, trajectory[i].y, 4, 0, 2 * Math.PI);
    ctx.fill();
  }

  if (posY < canvas.height) {
    ctx.fillStyle = "#fff";
    ctx.beginPath();
    ctx.arc(posX, posY, 8, 0, 2 * Math.PI);
    ctx.fill();
  }

  time += 0.05;
  requestAnimationFrame(draw);
}

reset();
draw();
