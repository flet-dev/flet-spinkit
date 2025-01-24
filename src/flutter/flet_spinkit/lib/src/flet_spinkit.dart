import 'package:flet/flet.dart';
import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';

class FletSpinkitControl extends StatelessWidget {
  final Control? parent;
  final Control control;

  const FletSpinkitControl({
    super.key,
    required this.parent,
    required this.control,
  });

  @override
  Widget build(BuildContext context) {
    var color = control.attrColor("color", context);
    var size = control.attrDouble("size");
    Widget myControl = SpinKitRotatingCircle(
      color: color,
      size: size ?? 100,
    );


    return constrainedControl(context, myControl, parent, control);
  }
}
