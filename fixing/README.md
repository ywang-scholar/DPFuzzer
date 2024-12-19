# Fix Vulnerabilities
## Case1
Adjusted parameters
```bash
optimization/lambda_smooth:     1.0 -> 0.4
optimization/lambda_collision:  1.0 -> 3.0
```
<p align = "center">
<div style="position: relative; display: inline-block;">
  <div style="position: absolute; top: 0; left: 0; background-color: rgba(255, 255, 255, 0.9); padding: 8px;">
    <b style="font-size: 32px;">Before</b>
  </div>
  <img src="type1/before.gif" alt="image" style="width: auto; height: 360px;">
</div>

<div style="position: relative; display: inline-block;">
  <div style="position: absolute; top: 0; left: 0; background-color: rgba(255, 255, 255, 0.9); padding: 8px;">
    <b style="font-size: 32px;">After</b>
  </div>
  <img src="type1/after.gif" alt="image" style="width: auto; height: 360px;">
</div>
</p>

## Case2
Adjusted parameters
```bash
manager/feasibility_tolerance:  0.05 -> 0.15
optimization/lambda_smooth:     1.0 -> 0.6
```
<p align = "center">
<div style="position: relative; display: inline-block;">
  <div style="position: absolute; top: 0; left: 0; background-color: rgba(255, 255, 255, 0.9); padding: 8px;">
    <b style="font-size: 32px;">Before</b>
  </div>
  <img src="type3/before.gif" alt="image" style="width: auto; height: 360px;">
</div>

<div style="position: relative; display: inline-block;">
  <div style="position: absolute; top: 0; left: 0; background-color: rgba(255, 255, 255, 0.9); padding: 8px;">
    <b style="font-size: 32px;">After</b>
  </div>
  <img src="type3/after.gif" alt="image" style="width: auto; height: 360px;">
</div>
</p>